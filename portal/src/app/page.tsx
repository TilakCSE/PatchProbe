"use client";

import { ChangeEvent, useMemo, useState } from "react";

const LABELS = [
  "API/code compatibility",
  "Configuration/deployment",
  "Data/schema migration",
  "UI/output behavior",
  "No targeted check stated",
] as const;

type Prediction = {
  label: string;
  score: number;
  scores: Record<string, number>;
};
type ModelInfo = {
  version: string;
  sha256: string;
  trainedOn: string;
  warning: string;
};
type ReviewRow = {
  id: string;
  text: string;
  source: string;
  prediction?: Prediction;
  decision: string;
  reason: string;
};
type Mode = "classify" | "batch" | "review" | "about";

function parseCsv(input: string): string[][] {
  const rows: string[][] = [];
  let row: string[] = [];
  let cell = "";
  let quoted = false;
  const source = input.replace(/^\uFEFF/, "");
  for (let i = 0; i < source.length; i += 1) {
    const ch = source[i];
    if (ch === '"') {
      if (quoted && source[i + 1] === '"') {
        cell += '"';
        i += 1;
      } else {
        quoted = !quoted;
      }
    } else if (ch === "," && !quoted) {
      row.push(cell);
      cell = "";
    } else if ((ch === "\n" || ch === "\r") && !quoted) {
      if (ch === "\r" && source[i + 1] === "\n") i += 1;
      row.push(cell);
      if (row.some((value) => value.trim())) rows.push(row);
      row = [];
      cell = "";
    } else {
      cell += ch;
    }
  }
  if (quoted) throw new Error("The CSV has an unclosed quoted field.");
  row.push(cell);
  if (row.some((value) => value.trim())) rows.push(row);
  return rows;
}

function safeSourceUrl(value: string): string | undefined {
  try {
    const url = new URL(value);
    return url.protocol === "http:" || url.protocol === "https:" ? url.toString() : undefined;
  } catch {
    return undefined;
  }
}

function escapeCsv(value: string): string {
  const safe = /^[=+@-]/.test(value.trimStart()) ? "'" + value : value;
  return '"' + safe.replaceAll('"', '""') + '"';
}

function saveCsv(filename: string, rows: string[][]) {
  const body = rows.map((row) => row.map(escapeCsv).join(",")).join("\r\n");
  const url = URL.createObjectURL(new Blob(["\uFEFF", body], { type: "text/csv;charset=utf-8" }));
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(url);
}

function scoreText(value?: number) {
  return typeof value === "number" && Number.isFinite(value)
    ? Math.round(value * 100) + "%"
    : "—";
}

async function readError(response: Response): Promise<string> {
  try {
    const data = await response.json();
    return data?.error?.message || "The prediction service could not complete this request.";
  } catch {
    return "The prediction service could not complete this request.";
  }
}

export default function Home() {
  const [mode, setMode] = useState<Mode>("classify");
  const [note, setNote] = useState("");
  const [single, setSingle] = useState<Prediction | null>(null);
  const [model, setModel] = useState<ModelInfo | null>(null);
  const [rows, setRows] = useState<ReviewRow[]>([]);
  const [selected, setSelected] = useState(0);
  const [fileName, setFileName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const [notice, setNotice] = useState("");

  const reviewed = useMemo(() => rows.filter((row) => row.decision).length, [rows]);
  const active = rows[selected];
  const activeSourceUrl = active ? safeSourceUrl(active.source) : undefined;

  async function predictOne() {
    const clean = note.trim();
    setError("");
    setNotice("");
    setSingle(null);
    if (!clean) return setError("Paste a release-note entry to classify.");
    if (clean.length > 10000) return setError("Keep each note below 10,000 characters.");
    setBusy(true);
    try {
      const response = await fetch("/api/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: clean }),
      });
      if (!response.ok) throw new Error(await readError(response));
      const data = await response.json();
      setSingle(data.prediction);
      setModel(data.model);
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Prediction failed.");
    } finally {
      setBusy(false);
    }
  }

  async function loadFile(event: ChangeEvent<HTMLInputElement>) {
    const file = event.target.files?.[0];
    if (!file) return;
    if (file.size > 2_000_000) { setError("Use a CSV smaller than 2 MB."); event.target.value = ""; return; }
    setError("");
    setNotice("");
    try {
      const parsed = parseCsv(await file.text());
      if (parsed.length < 2) throw new Error("The CSV needs a header and at least one note.");
      const headers = parsed[0].map((name) => name.trim().toLowerCase());
      const textIndex = headers.findIndex((name) => ["text", "note", "release_note", "entry"].includes(name));
      if (textIndex < 0) throw new Error("Add a text column named text, note, release_note, or entry.");
      const idIndex = headers.findIndex((name) => ["id", "entry_id"].includes(name));
      const sourceIndex = headers.findIndex((name) => ["source", "source_url", "url"].includes(name));
      const imported = parsed.slice(1).map((cells, index) => ({
        id: (idIndex >= 0 ? cells[idIndex] : "") || String(index + 1),
        text: (cells[textIndex] || "").trim(),
        source: (sourceIndex >= 0 ? cells[sourceIndex] : "") || "",
        decision: "",
        reason: "",
      })).filter((row) => row.text);
      if (!imported.length) throw new Error("No nonempty notes were found in the text column.");
      if (imported.length > 100) throw new Error("Use at most 100 notes per batch.");
      if (imported.some((row) => row.text.length > 10000)) throw new Error("A note exceeds 10,000 characters.");
      setRows(imported);
      setSelected(0);
      setFileName(file.name);
      setNotice(imported.length + " notes loaded. Run the classifier to add suggestions.");
      setMode("batch");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "The CSV could not be read.");
    }
    event.target.value = "";
  }

  async function predictBatch() {
    if (!rows.length) return setError("Import a CSV first.");
    setBusy(true);
    setError("");
    setNotice("");
    try {
      const response = await fetch("/api/predict/batch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ texts: rows.map((row) => row.text) }),
      });
      if (!response.ok) throw new Error(await readError(response));
      const data = await response.json();
      if (!Array.isArray(data.predictions) || data.predictions.length !== rows.length) {
        throw new Error("The service returned an incomplete batch. No rows were changed.");
      }
      setRows((current) => current.map((row, index) => ({
        ...row,
        prediction: data.predictions[index],
      })));
      setModel(data.model);
      setNotice("Suggestions are ready. Review them before using the CSV as decisions.");
    } catch (cause) {
      setError(cause instanceof Error ? cause.message : "Batch prediction failed.");
    } finally {
      setBusy(false);
    }
  }

  function editDecision(field: "decision" | "reason", value: string) {
    setRows((current) => current.map((row, index) =>
      index === selected ? { ...row, [field]: value } : row
    ));
  }

  function exportResults() {
    if (!rows.length) return;
    saveCsv("patchprobe-predictions.csv", [
      ["id", "text", "source_url", "suggested_label", "score_uncalibrated", "model_version"],
      ...rows.map((row) => [
        row.id, row.text, row.source, row.prediction?.label || "",
        row.prediction ? String(row.prediction.score) : "", model?.version || "",
      ]),
    ]);
  }

  function exportReviews() {
    if (!rows.length || !reviewed) return;
    saveCsv("patchprobe-review-draft.csv", [
      ["id", "text", "source_url", "suggested_label", "review_decision", "review_reason", "model_version"],
      ...rows.filter((row) => row.decision).map((row) => [
        row.id, row.text, row.source, row.prediction?.label || "",
        row.decision, row.reason, model?.version || "",
      ]),
    ]);
  }

  return (
    <div className="app-shell">
      <aside className="sidebar">
        <a className="brand" href="#top" aria-label="PatchProbe home">
          <span className="brand-mark">P<span>.</span></span>
          <span><strong>PatchProbe</strong><small>Release note triage</small></span>
        </a>
        <div className="sidebar-label">WORKSPACE</div>
        <nav aria-label="Main navigation">
          {([
            ["classify", "01", "Classify one note"],
            ["batch", "02", "Batch workspace"],
            ["review", "03", "Human review"],
            ["about", "04", "Method & limits"],
          ] as const).map(([key, number, label]) => (
            <button key={key} type="button" className={"nav-item " + (mode === key ? "active" : "")}
              onClick={() => { setMode(key); setError(""); setNotice(""); }}>
              <span>{number}</span>{label}
            </button>
          ))}
        </nav>
        <div className="sidebar-bottom">
          <div className="sidebar-rule" />
          <p>Built for a first check after a software upgrade.</p>
          <span className="quiet-chip">Research MVP</span>
        </div>
      </aside>

      <main className="main" id="top">
        <header className="topbar">
          <span>PATCHPROBE / WORKSPACE</span>
          <span className="topbar-right"><i /> Local review workflow</span>
        </header>

        <div className="content">
          <div className="eyebrow"><span className="eyebrow-line" /> SOFTWARE CHANGE INTELLIGENCE</div>
          <div className="hero-row">
            <div>
              <h1>{mode === "classify" ? "Know what to check first." :
                mode === "batch" ? "Triage a release in one pass." :
                mode === "review" ? "Keep the human decision." :
                "A focused NLP workflow."}</h1>
              <p className="lead">{mode === "classify"
                ? "Paste one release-note entry. PatchProbe suggests the first area a developer should verify after upgrading."
                : mode === "batch"
                  ? "Import up to 100 release-note entries, inspect the suggestions, and export a working CSV."
                  : mode === "review"
                    ? "Confirm, change, or mark each suggestion unclear. Your review stays in this browser until you export it."
                    : "A transparent classifier for downstream verification areas, trained on human-confirmed Django release notes."}</p>
            </div>
            <div className="hero-index">PP / 01</div>
          </div>

          {error && <div className="alert error" role="alert"><strong>Needs attention</strong><span>{error}</span></div>}
          {notice && <div className="alert notice" role="status"><strong>Updated</strong><span>{notice}</span></div>}

          {mode === "classify" && (
            <div className="workspace-grid">
              <section className="panel input-panel">
                <div className="panel-heading"><div><span className="step">01 — INPUT</span><h2>Release-note entry</h2></div><span className="panel-aside">Plain text</span></div>
                <label htmlFor="note">Paste the specific change</label>
                <textarea id="note" value={note} maxLength={10001} onChange={(event) => setNote(event.target.value)}
                  placeholder="For example: A method has been deprecated and will be removed in the next release…" />
                <div className="field-footer"><span>Use one substantive bullet or short paragraph, without a section heading.</span><span>{note.length.toLocaleString()} / 10,000</span></div>
                <div className="action-row">
                  <button className="primary-btn" type="button" disabled={busy} onClick={predictOne}>{busy ? "Classifying…" : "Classify note"}<span aria-hidden>↗</span></button>
                  <button className="text-btn" type="button" onClick={() => { setNote(""); setSingle(null); setError(""); }}>Clear</button>
                </div>
              </section>
              <section className="panel result-panel" aria-live="polite">
                <div className="panel-heading"><div><span className="step">02 — SUGGESTION</span><h2>First area to verify</h2></div><span className="panel-aside">Model output</span></div>
                {single ? (
                  <>
                    <div className="result-label">{single.label}</div>
                    <p className="muted">Suggested review priority based on the note text. Verify the affected feature in your own application.</p>
                    <div className="score-block"><span>Relative model score</span><strong>{scoreText(single.score)}</strong></div>
                    <div className="score-list">
                      {LABELS.map((label) => (
                        <div className="score-row" key={label}><span>{label}</span><div className="score-track"><i style={{ width: scoreText(single.scores?.[label]) }} /></div><b>{scoreText(single.scores?.[label])}</b></div>
                      ))}
                    </div>
                  </>
                ) : (
                  <div className="empty-state"><div className="empty-icon">⌁</div><h3>Your result will appear here</h3><p>Enter an entry and run the classifier to see its suggested check area and score breakdown.</p></div>
                )}
                <div className="model-foot">Scores are uncalibrated. Treat suggestions as review aids, not proof of safety.</div>
              </section>
            </div>
          )}

          {mode === "batch" && (
            <div className="stack">
              <div className="workspace-grid">
                <section className="panel">
                  <div className="panel-heading"><div><span className="step">01 — IMPORT</span><h2>Bring your notes</h2></div><span className="panel-aside">CSV · 100 max</span></div>
                  <label className="upload" htmlFor="csv-file"><span className="upload-icon">↑</span><strong>{fileName || "Choose a CSV file"}</strong><small>Needs a text, note, release_note, or entry column. Optional id and source_url.</small></label>
                  <input id="csv-file" className="file-input" type="file" accept=".csv,text/csv" onChange={loadFile} />
                  <div className="action-row"><button className="primary-btn" type="button" onClick={predictBatch} disabled={busy || !rows.length}>{busy ? "Classifying…" : "Classify batch"}<span aria-hidden>↗</span></button><span className="muted">{rows.length} notes loaded</span></div>
                </section>
                <section className="panel batch-summary">
                  <div className="panel-heading"><div><span className="step">02 — OUTPUT</span><h2>Working set</h2></div></div>
                  <div className="stat-line"><strong>{rows.length}</strong><span>entries in this batch</span></div>
                  <div className="stat-line"><strong>{rows.filter((row) => row.prediction).length}</strong><span>model suggestions ready</span></div>
                  <div className="summary-actions"><button className="secondary-btn" type="button" onClick={exportResults} disabled={!rows.some((row) => row.prediction)}>Export predictions ↓</button><button className="text-btn" type="button" onClick={() => setMode("review")} disabled={!rows.length}>Open human review →</button></div>
                </section>
              </div>
              <section className="panel table-panel">
                <div className="panel-heading"><div><span className="step">03 — INSPECT</span><h2>Entry overview</h2></div><span className="panel-aside">{rows.length ? rows.length + " rows" : "No rows yet"}</span></div>
                <div className="table-scroll"><table><thead><tr><th>ID</th><th>Release-note text</th><th>Suggested first check</th><th>Score*</th></tr></thead><tbody>{rows.length ? rows.map((row, index) => <tr key={index}><td>{row.id}</td><td className="text-cell">{row.text}</td><td>{row.prediction?.label || "Awaiting model"}</td><td>{scoreText(row.prediction?.score)}</td></tr>) : <tr><td colSpan={4} className="table-empty">Import a CSV to start a batch.</td></tr>}</tbody></table></div>
                <p className="table-caption">* Scores are uncalibrated. Exported suggestions are not human labels.</p>
              </section>
            </div>
          )}

          {mode === "review" && (
            <div className="stack">
              <div className="review-top"><div><span className="step">HUMAN-IN-THE-LOOP</span><h2>Review queue</h2><p className="muted">A decision is saved in browser memory for this session and included only when you export the review draft.</p></div><div className="review-progress"><strong>{reviewed} / {rows.length}</strong><span>decisions made</span></div></div>
              {!rows.length ? <div className="panel empty-review"><h3>No notes in the queue</h3><p>Import a CSV in the batch workspace to begin a review session.</p><button className="primary-btn" onClick={() => setMode("batch")}>Go to batch workspace <span>↗</span></button></div> : <>
                <div className="review-layout">
                  <aside className="panel queue-list" aria-label="Review entries">{rows.map((row, index) => <button key={index} className={"queue-item " + (selected === index ? "selected" : "")} onClick={() => setSelected(index)}><span className="queue-number">{String(index + 1).padStart(2, "0")}</span><span className="queue-copy">{row.text}</span><span className={"queue-dot " + (row.decision ? "done" : "")} /></button>)}</aside>
                  <section className="panel review-detail">
                    <div className="panel-heading"><div><span className="step">ENTRY {selected + 1} / {rows.length}</span><h2>Make the final call</h2></div><span className="panel-aside">{active.id}</span></div>
                    <blockquote>{active.text}</blockquote>
                    {activeSourceUrl && <a className="source-link" href={activeSourceUrl} target="_blank" rel="noreferrer">Open original source ↗</a>}
                    <div className="suggestion-strip"><span>MODEL SUGGESTION</span><strong>{active.prediction?.label || "Run batch classification first"}</strong><small>{active.prediction ? scoreText(active.prediction.score) + " relative score · uncalibrated" : ""}</small></div>
                    <fieldset><legend>Your decision</legend><div className="choice-grid">{[...LABELS, "UNCLEAR"].map((label) => <label key={label} className={"choice " + (active.decision === label ? "checked" : "")}><input type="radio" name={"decision-" + selected} checked={active.decision === label} onChange={() => editDecision("decision", label)} />{label}</label>)}</div></fieldset>
                    <label className="reason-label" htmlFor="reason">Reason or reviewer note <span>{active.decision === "UNCLEAR" ? "Required for UNCLEAR" : "Optional"}</span></label>
                    <textarea id="reason" className="reason-box" value={active.reason} onChange={(event) => editDecision("reason", event.target.value)} placeholder="What in the note supports this decision?" />
                    <div className="review-actions"><button className="secondary-btn" disabled={selected === 0} onClick={() => setSelected(selected - 1)}>← Previous</button><button className="primary-btn" disabled={selected >= rows.length - 1 || (active.decision === "UNCLEAR" && !active.reason.trim())} onClick={() => setSelected(selected + 1)}>Next entry <span>→</span></button></div>
                  </section>
                </div>
                <div className="export-bar"><div><strong>Export your review draft</strong><span>Only decided rows are exported. Verify decisions before adding them to any training set.</span></div><button className="secondary-btn" onClick={exportReviews} disabled={!reviewed || rows.some((row) => row.decision === "UNCLEAR" && !row.reason.trim())}>Export {reviewed} decisions ↓</button></div>
              </>}
            </div>
          )}

          {mode === "about" && (
            <div className="stack">
              <div className="metric-grid"><div className="metric-card"><strong>571</strong><span>source entries</span></div><div className="metric-card"><strong>531</strong><span>model labels</span></div><div className="metric-card"><strong>13</strong><span>unclear reviews</span></div><div className="metric-card"><strong>27</strong><span>excluded fragments</span></div></div>
              <div className="workspace-grid about-grid"><section className="panel"><span className="step">THE METHOD</span><h2>From note to first check</h2><ol className="method-list"><li>Extract entries from pinned, official Django release notes.</li><li>Review and label the first area a developer should verify.</li><li>Learn word and character TF-IDF features from training text.</li><li>Use balanced logistic regression to suggest one of five areas.</li><li>Show the suggestion for a person to accept or correct.</li></ol></section><section className="panel"><span className="step">THE BOUNDARY</span><h2>What this can and cannot say</h2><p>PatchProbe is a research MVP. It suggests where to begin verification; it does not analyze your code, detect actual breakage, or certify an upgrade.</p><p>The training data comes from Django. Other products may use different vocabulary and structure. Cross-company results are exploratory until independently labeled evaluation data exists.</p><p>The fifth class, “No targeted check stated,” has only five confirmed examples. Scores shown here are uncalibrated and are not probabilities of correctness.</p></section></div>
              <section className="panel taxonomy"><span className="step">THE FIVE AREAS</span><h2>Classification guide</h2><div className="taxonomy-grid">{LABELS.map((label, index) => <div key={label}><span>{String(index + 1).padStart(2, "0")}</span><strong>{label}</strong><p>{["Calls, imports, signatures, exceptions, and integration code.", "Settings, runtime requirements, packaging, and deployments.", "Database schema, ORM data semantics, migrations, and storage.", "Rendered pages, forms, responses, and user-visible output.", "A substantive note with no concrete downstream check stated."][index]}</p></div>)}</div></section>
            </div>
          )}
          <footer className="footer"><span>PATCHPROBE · NAVRACHANA UNIVERSITY</span><span>{model ? "Model " + model.version + " · " + model.sha256.slice(0, 10) : "Model status shown after prediction"}</span></footer>
          {model?.warning && <p className="runtime-warning" role="status">{model.warning}</p>}
        </div>
      </main>
    </div>
  );
}





