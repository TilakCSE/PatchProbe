// Dependency-free inference for the exported sklearn pipeline.
// Python-vs-Node parity checks exercise this exact module.
export function validateModel(model) {
  if (model.formatVersion !== 1 || model.classes?.length !== 5 ||
      model.word?.analyzer !== "word" || model.char?.analyzer !== "char_wb" ||
      model.word.idf.length + model.char.idf.length !== model.classifier?.coef?.[0]?.length ||
      model.classifier.coef.length !== model.classes.length ||
      model.classifier.intercept.length !== model.classes.length ||
      !/^[a-f0-9]{64}$/.test(model.model?.sha256 ?? "")) {
    throw new Error("Invalid or incomplete PatchProbe serving model");
  }
}

function terms(text, vectorizer) {
  const counts = new Map();
  const add = (token) => counts.set(token, (counts.get(token) ?? 0) + 1);
  const lower = text.toLowerCase();
  if (vectorizer.analyzer === "word") {
    const words = lower.match(/[\p{L}\p{N}_]{2,}/gu) ?? [];
    for (let n = vectorizer.ngramRange[0]; n <= vectorizer.ngramRange[1]; n++) {
      for (let i = 0; i + n <= words.length; i++) add(words.slice(i, i + n).join(" "));
    }
  } else {
    const normalized = lower.replace(/\s\s+/gu, " ");
    for (const word of normalized.split(/\s+/u).filter(Boolean)) {
      const padded = Array.from(` ${word} `);
      for (let n = vectorizer.ngramRange[0]; n <= vectorizer.ngramRange[1]; n++) {
        if (padded.length <= n) {
          add(padded.join(""));
          break;
        }
        for (let i = 0; i + n <= padded.length; i++) add(padded.slice(i, i + n).join(""));
      }
    }
  }
  return counts;
}

function sparseVector(text, vectorizer, offset) {
  const values = [];
  let squared = 0;
  for (const [term, count] of terms(text, vectorizer)) {
    if (!Object.prototype.hasOwnProperty.call(vectorizer.vocabulary, term)) continue;
    const index = vectorizer.vocabulary[term];
    const value = (vectorizer.sublinearTf ? 1 + Math.log(count) : count) * vectorizer.idf[index];
    values.push([index + offset, value]);
    squared += value * value;
  }
  const norm = Math.sqrt(squared);
  return norm ? values.map(([index, value]) => [index, value / norm]) : [];
}

export function predictWithModel(model, text) {
  const features = [
    ...sparseVector(text, model.word, 0),
    ...sparseVector(text, model.char, model.word.idf.length),
  ];
  const logits = model.classifier.coef.map((row, classIndex) => {
    let value = model.classifier.intercept[classIndex];
    for (const [index, feature] of features) value += row[index] * feature;
    return value;
  });
  const maximum = Math.max(...logits);
  const exponentials = logits.map((value) => Math.exp(value - maximum));
  const total = exponentials.reduce((a, b) => a + b, 0);
  const probabilities = exponentials.map((value) => value / total);
  const winner = probabilities.indexOf(Math.max(...probabilities));
  return {
    label: model.classes[winner],
    score: probabilities[winner],
    scores: Object.fromEntries(model.classes.map((label, index) => [label, probabilities[index]])),
  };
}
