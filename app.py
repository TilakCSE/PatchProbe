"""Guided human annotation and optional local-model review interface.

Run with: streamlit run app.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

import pandas as pd
import streamlit as st

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from patchprobe.annotation import (  # noqa: E402
    ALL_CHOICES,
    LABEL_DEFINITIONS,
    UNCLEAR,
    AnnotationError,
    load_entries,
    load_labels,
    next_unreviewed,
    progress,
    save_annotation,
)
from patchprobe.inference import (  # noqa: E402
    artifact_status,
    load_local_model,
    predict_review,
)


DEFAULT_ENTRIES = "data/processed/pilot_queue.csv"
DEFAULT_LABELS = "data/annotations/pilot_labels.csv"
PROJECT_ROOT = Path(__file__).resolve().parent
CORPUS_PATH = PROJECT_ROOT / "data/processed/annotated_corpus.csv"
PREDICTIONS_PATH = PROJECT_ROOT / "artifacts/model/predictions.csv"
EXTERNAL_RESULTS_PATH = PROJECT_ROOT / "data/external/probe_results.csv"


def _safe_source_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _corpus_view() -> None:
    st.title("PatchProbe: reviewed corpus")
    st.caption("Explore every pinned Django note and its human-confirmed disposition. These rows are source data and review decisions, not model predictions.")
    if not CORPUS_PATH.is_file():
        st.error("The reviewed corpus is missing. Run scripts/build_annotated_corpus.py from the project root.")
        return
    with CORPUS_PATH.open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    decisions = Counter(row["review_decision"] for row in rows)
    model_ready = sum(bool(row["model_label"]) for row in rows)
    total_col, usable_col, unclear_col, excluded_col = st.columns(4)
    total_col.metric("Source notes", len(rows))
    usable_col.metric("Model labels", model_ready)
    unclear_col.metric("Unclear", decisions["UNCLEAR"])
    excluded_col.metric("Excluded", decisions["EXCLUDE"])

    st.subheader("Label coverage")
    chart_rows = [
        {"First check area": label, "Reviewed notes": decisions[label]}
        for label in LABEL_DEFINITIONS
    ]
    st.bar_chart(pd.DataFrame(chart_rows).set_index("First check area"), horizontal=True)
    st.caption("The small 'No targeted check stated' class remains a key model limitation. UNCLEAR and EXCLUDE are not training labels.")

    st.subheader("Inspect entries")
    release_options = sorted({row["release"] for row in rows})
    selected_releases = st.multiselect("Release", release_options, default=release_options)
    decision_options = list(LABEL_DEFINITIONS) + ["UNCLEAR", "EXCLUDE"]
    selected_decisions = st.multiselect("Review decision", decision_options, default=decision_options)
    search = st.text_input("Find text", placeholder="Search the cleaned note text or entry ID").casefold().strip()
    filtered = [
        row for row in rows
        if row["release"] in selected_releases
        and row["review_decision"] in selected_decisions
        and (not search or search in row["text"].casefold() or search in row["entry_id"].casefold())
    ]
    st.caption(f"Showing {len(filtered)} of {len(rows)} source notes")
    visible_columns = ["entry_id", "release", "text", "review_decision", "source_url"]
    st.dataframe(
        pd.DataFrame(filtered, columns=visible_columns),
        width="stretch",
        hide_index=True,
        column_config={"source_url": st.column_config.LinkColumn("Official source")},
    )
    if filtered:
        selected_id = st.selectbox("Read a full entry", [row["entry_id"] for row in filtered])
        selected = next(row for row in filtered if row["entry_id"] == selected_id)
        st.write(selected["text"])
        st.caption(f"Django {selected['release']} · {selected['review_decision']} · {selected['section_path']}")
        if selected["review_note"]:
            st.caption(f"Review note: {selected['review_note']}")
        if _safe_source_url(selected["source_url"]):
            st.link_button("Open official release note", selected["source_url"])


def _evaluation_view(metrics: dict) -> None:
    st.title("PatchProbe: full-corpus evaluation")
    st.caption("Release-held-out Django results for the fixed TF-IDF and logistic-regression recipe. The displayed model is fitted on training releases only.")
    test = metrics.get("evaluation", {}).get("test", {})
    model = test.get("model", {})
    majority = test.get("majority", {})
    keyword = test.get("keyword", {})
    if not model:
        st.error("Evaluation metrics are incomplete. Regenerate them with scripts/train_full_corpus.py.")
        return
    test_count, accuracy, macro_f1, baseline_f1 = st.columns(4)
    test_count.metric("Held-out test notes", model.get("n", "?"))
    accuracy.metric("Test accuracy", f"{model.get('accuracy', 0):.1%}")
    macro_f1.metric("Five-label macro-F1", f"{model.get('macro_f1_five_labels', 0):.3f}")
    baseline_f1.metric("Keyword macro-F1", f"{keyword.get('macro_f1_five_labels', 0):.3f}")
    st.warning("Pilot evaluation: the fifth class has only five training examples and zero development or test examples. Its test recall cannot be measured. The all-label portal model is a separate fit and has no held-out score of its own.")

    split_counts = metrics.get("split_counts", {})
    audit = metrics.get("near_duplicate_audit", {})
    st.caption(
        f"Chronological release split after similarity filtering: {split_counts.get('train', '?')} train / "
        f"{split_counts.get('dev', '?')} dev / {split_counts.get('test', '?')} test. "
        f"{audit.get('excluded_model_rows', '?')} cross-split near-duplicate rows excluded from evaluation."
    )
    st.subheader("Baselines and class results")
    st.dataframe(pd.DataFrame([
        {"Method": "TF-IDF + logistic regression", "Accuracy": model.get("accuracy"), "Five-label macro-F1": model.get("macro_f1_five_labels")},
        {"Method": "Majority class", "Accuracy": majority.get("accuracy"), "Five-label macro-F1": majority.get("macro_f1_five_labels")},
        {"Method": "Fixed keyword rules", "Accuracy": keyword.get("accuracy"), "Five-label macro-F1": keyword.get("macro_f1_five_labels")},
    ]), width="stretch", hide_index=True)
    per_class = model.get("per_class", {})
    st.dataframe(pd.DataFrame([
        {"First check area": label, "Support": per_class.get(label, {}).get("support", 0),
         "Precision": per_class.get(label, {}).get("precision", 0),
         "Recall": per_class.get(label, {}).get("recall", 0),
         "F1": per_class.get(label, {}).get("f1-score", 0)}
        for label in LABEL_DEFINITIONS
    ]), width="stretch", hide_index=True)

    st.subheader("Confusion matrix")
    labels = list(LABEL_DEFINITIONS)
    matrix = model.get("confusion_matrix", [])
    if len(matrix) == len(labels):
        st.dataframe(pd.DataFrame(matrix, index=labels, columns=labels), width="stretch")
        st.caption("Rows are human-confirmed labels; columns are model predictions on the held-out Django notes.")

    if PREDICTIONS_PATH.is_file():
        with PREDICTIONS_PATH.open("r", encoding="utf-8-sig", newline="") as stream:
            predictions = list(csv.DictReader(stream))
        errors = [row for row in predictions if row["split"] == "test" and row["correct"] == "False"]
        st.subheader(f"Held-out errors ({len(errors)})")
        st.dataframe(pd.DataFrame(errors, columns=("entry_id", "release", "text", "gold_label", "predicted_label", "source_url")),
                     width="stretch", hide_index=True,
                     column_config={"source_url": st.column_config.LinkColumn("Official source")})

    st.subheader("External product probe")
    st.info("These 15 React, VS Code, and Chrome references were proposed by an agent, not independently human-labeled. Agreement is exploratory and is not cross-product accuracy.")
    if EXTERNAL_RESULTS_PATH.is_file():
        with EXTERNAL_RESULTS_PATH.open("r", encoding="utf-8-sig", newline="") as stream:
            external = list(csv.DictReader(stream))
        agreed = sum(row["agrees_with_agent_proposal"] == "True" for row in external)
        st.caption(f"{agreed} of {len(external)} predictions match the proposed interpretations; 2 of 5 per product in this fixed probe.")
        st.dataframe(pd.DataFrame(external, columns=("probe_id", "product", "text", "proposed_reference_label", "predicted_label", "source_url")),
                     width="stretch", hide_index=True,
                     column_config={"source_url": st.column_config.LinkColumn("Official source")})


def _prediction_view(metrics: dict) -> None:
    st.title("PatchProbe: prediction review")
    st.caption("Paste a Django release-note entry to see a suggested first check area. A developer still reviews the note and plans the actual checks.")
    if metrics.get("status") == "pilot":
        st.warning("This full-corpus model is still a pilot: the fifth class has no development or test examples. Treat every output as a review suggestion.")
    else:
        st.info("The model has a recorded five-class evaluation. Check metrics.json and the model card for test support and failure cases.")
    counts = metrics.get("counts", {})
    if isinstance(counts, dict):
        st.caption(f"Labeled dataset: {counts.get('accepted', 'unknown')} accepted rows; {counts.get('unclear', 'unknown')} UNCLEAR rows excluded.")

    with st.form("prediction_input"):
        note_text = st.text_area("Release-note text", height=180, placeholder="Paste one substantive release-note bullet or short paragraph.")
        submitted = st.form_submit_button("Suggest first check area", type="primary")
    if not submitted:
        return
    try:
        model = load_local_model(PROJECT_ROOT)
        result = predict_review(model, note_text)
    except Exception as error:  # A damaged local joblib artifact may raise several deserialization errors.
        st.error(f"Prediction unavailable: {error}")
        return

    st.subheader(f"Suggested area: {result.predicted_label}")
    st.warning("Review the original note before acting. This suggestion does not prove an upgrade is safe or that every app needs this check.")
    st.markdown("**Full class scores (uncalibrated)**")
    st.table([
        {"First check area": label, "Uncalibrated model score": f"{score:.1%}" if score is not None else "Not present in fitted model"}
        for label, score in result.scores.items()
    ])
    st.caption("Scores are logistic-regression outputs, not calibrated probabilities of correctness.")
    st.caption("For source-linked notes and saved human decisions, open Reviewed corpus.")


def main() -> None:
    st.set_page_config(page_title="PatchProbe review", page_icon="🧩", layout="wide")
    model_status = artifact_status(PROJECT_ROOT)
    with st.sidebar:
        st.header("PatchProbe mode")
        choices = ["Reviewed corpus", "Guided annotation (pilot)"]
        if model_status.available:
            choices.append("Model evaluation")
            choices.append("Prediction review")
        workspace_mode = st.radio("Choose a mode", choices)
        if not model_status.available:
            st.info(model_status.reason)

    if workspace_mode == "Reviewed corpus":
        _corpus_view()
        return
    if workspace_mode == "Model evaluation":
        _evaluation_view(model_status.metrics or {})
        return
    if workspace_mode == "Prediction review":
        _prediction_view(model_status.metrics or {})
        return

    st.title("PatchProbe: guided annotation pilot")
    st.caption("This screen preserves the original 50-row review workflow. The complete 571-row confirmed corpus is in Reviewed corpus. A saved choice here is a human decision, not a model prediction.")

    with st.sidebar:
        st.header("Review session")
        entries_path = Path(st.text_input("Entries CSV", DEFAULT_ENTRIES)).expanduser()
        labels_path = Path(st.text_input("Saved labels CSV", DEFAULT_LABELS)).expanduser()
        annotator = st.text_input("Your name", help="Stored with each decision.")
        st.caption("Decisions are saved in the labels CSV. Skips last only for this browser session.")

    if not entries_path.is_file():
        st.info(
            f"No entries found at `{entries_path}` yet. Generate the dataset first, or set the Entries CSV path in the sidebar."
        )
        st.stop()

    try:
        entries = load_entries(entries_path)
        valid_ids = {row["entry_id"] for row in entries}
        labels = load_labels(labels_path, valid_ids)
    except (AnnotationError, OSError, UnicodeError) as error:
        st.error(f"Could not load review data: {error}")
        st.stop()

    if not entries:
        st.info("The entries CSV has no rows. Extract or select a pilot before reviewing.")
        st.stop()

    session_key = (str(entries_path.resolve()), str(labels_path.resolve()))
    if st.session_state.get("annotation_dataset") != session_key:
        st.session_state.annotation_dataset = session_key
        st.session_state.skipped_ids = set()

    counts = progress(entries, labels)
    reviewed_col, remaining_col, unclear_col = st.columns(3)
    reviewed_col.metric("Reviewed", f"{counts['reviewed']} / {counts['total']}")
    remaining_col.metric("Remaining", counts["remaining"])
    unclear_col.metric("Unclear", counts["unclear"])
    st.progress(counts["reviewed"] / counts["total"])

    with st.expander("How to decide", expanded=True):
        st.write("Read the change itself, not its section heading. Pick the most specific interface explicitly affected in the note.")
        for label, definition in LABEL_DEFINITIONS.items():
            st.markdown(f"**{label}:** {definition}")
        st.markdown(
            "**UNCLEAR:** Two areas are equally primary, or the note is too underspecified to choose. "
            "Explain the ambiguity in the review note. UNCLEAR is excluded from five-class training."
        )
        st.caption(
            "Do not infer a database check from a model class or a UI check from a view alone. "
            "An internal fix with no downstream surface can be 'No targeted check stated'."
        )

    mode = st.radio("Review mode", ["Next unreviewed", "Revisit a saved decision"], horizontal=True)
    if mode == "Next unreviewed":
        row = next_unreviewed(entries, labels, st.session_state.skipped_ids)
        if row is None:
            if counts["remaining"] == 0:
                st.success("All entries have saved decisions.")
            else:
                st.info("All remaining entries were skipped in this session.")
                if st.button("Return to skipped entries"):
                    st.session_state.skipped_ids = set()
                    st.rerun()
            st.stop()
    else:
        reviewed = [entry for entry in entries if entry["entry_id"] in labels]
        if not reviewed:
            st.info("No saved decisions to revisit yet.")
            st.stop()
        by_id = {entry["entry_id"]: entry for entry in reviewed}
        selected_id = st.selectbox("Saved entry", list(by_id), format_func=lambda item: f"{item} — {by_id[item]['text'][:70]}")
        row = by_id[selected_id]

    entry_id = row["entry_id"]
    st.subheader(f"Entry {entry_id}")
    st.caption(f"Release: {row['release']}")
    st.write(row["text"])
    if _safe_source_url(row["source_url"]):
        st.link_button("Open official source", row["source_url"])
    else:
        st.caption(f"Source URL unavailable: {row['source_url'] or '(empty)'}")
    with st.expander("Source provenance", expanded=False):
        st.write(f"Section path: {row['section_path'] or '(none)'}")
        st.write(f"Source revision: {row['source_revision'] or '(unknown)'}")
        if row["raw_text"] and row["raw_text"] != row["text"]:
            st.write("Original extracted text:")
            st.write(row["raw_text"])

    with st.expander("Ask an agent for help with this row"):
        st.caption("Copy this into your chat if the distinction is hard. The saved choice remains yours.")
        st.code(
            "Help me apply the PatchProbe label guide to this Django release-note entry. "
            "Explain which phrases indicate a downstream check and whether two areas are equally primary. "
            "Do not save a label for me.\n\n"
            f"Entry ID: {entry_id}\nNote: {row['text']}",
            language=None,
        )

    previous = labels.get(entry_id)
    if previous:
        st.info(f"Saved: {previous['label']} by {previous['annotator']} at {previous['annotated_at']}. Saving again replaces this decision.")

    with st.form(f"decision_{entry_id}", clear_on_submit=False):
        options = ("Choose a label...",) + ALL_CHOICES
        default = options.index(previous["label"]) if previous else 0
        choice = st.selectbox("Your decision", options, index=default)
        note = st.text_area(
            "Review note",
            value=previous["review_note"] if previous else "",
            help="Optional for five labels; required for UNCLEAR. Cite the specific ambiguity if possible.",
        )
        submitted = st.form_submit_button("Save decision", type="primary")
    if submitted:
        if choice == options[0]:
            st.warning("Choose a label before saving.")
        else:
            try:
                save_annotation(
                    labels_path,
                    entry_id=entry_id,
                    label=choice,
                    annotator=annotator,
                    review_note=note,
                    valid_entry_ids=valid_ids,
                )
            except (AnnotationError, OSError) as error:
                st.error(f"Decision was not saved: {error}")
            else:
                st.session_state.skipped_ids.discard(entry_id)
                st.rerun()

    if mode == "Next unreviewed" and st.button("Skip for now"):
        st.session_state.skipped_ids.add(entry_id)
        st.rerun()

    with st.expander("Review counts by label"):
        for label, count in counts["by_label"].items():
            st.write(f"{label}: {count}")
        st.caption(f"Potential five-class rows: {counts['model_ready']}. Human review and held-out evaluation are still required.")


if __name__ == "__main__":
    main()
