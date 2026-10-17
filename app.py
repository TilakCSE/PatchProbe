"""Guided human annotation and optional local-model review interface.

Run with: streamlit run app.py
"""

from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import urlparse

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


def _safe_source_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def _prediction_view(metrics: dict) -> None:
    st.title("PatchProbe: prediction review")
    st.caption("Paste a Django release-note entry to see a suggested first check area. A developer still reviews the note and plans the actual checks.")
    if metrics.get("status") == "pilot":
        st.warning("This is a pilot model. Class support is below the planned evaluation threshold; treat every output as a demonstration suggestion.")
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
        {"First check area": label, "Uncalibrated model score": f"{score:.1%}" if score is not None else "Not trained in this pilot"}
        for label, score in result.scores.items()
    ])
    st.caption("Scores are logistic-regression outputs, not calibrated probabilities of correctness. A class absent from pilot training has no score.")
    st.caption("For a source-linked entry and a saved human decision, use Guided annotation.")


def main() -> None:
    st.set_page_config(page_title="PatchProbe review", page_icon="🧩", layout="centered")
    model_status = artifact_status(PROJECT_ROOT)
    with st.sidebar:
        st.header("PatchProbe mode")
        choices = ["Guided annotation"]
        if model_status.available:
            choices.append("Prediction review")
        workspace_mode = st.radio("Choose a mode", choices)
        if not model_status.available:
            st.info(model_status.reason)

    if workspace_mode == "Prediction review":
        _prediction_view(model_status.metrics or {})
        return

    st.title("PatchProbe: release-note review")
    st.caption("Choose the first downstream area to verify based on the note text. This is a human decision, not a model prediction.")

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
