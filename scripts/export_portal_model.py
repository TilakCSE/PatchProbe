"""Export the fitted TF-IDF/logistic model to portable JSON for Node inference.

Only export models trained by PatchProbe. Never load untrusted joblib files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import FeatureUnion, Pipeline


def _vectorizer_payload(vectorizer: TfidfVectorizer) -> dict:
    if vectorizer.binary or vectorizer.use_idf is False or vectorizer.norm != "l2":
        raise ValueError("Unsupported TF-IDF configuration")
    if vectorizer.strip_accents is not None or vectorizer.stop_words is not None:
        raise ValueError("Unsupported preprocessing configuration")
    return {
        "analyzer": vectorizer.analyzer,
        "ngramRange": list(vectorizer.ngram_range),
        "sublinearTf": vectorizer.sublinear_tf,
        "vocabulary": vectorizer.vocabulary_,
        "idf": vectorizer.idf_.tolist(),
    }


def export_model(model: Pipeline, *, version: str, trained_on: str, warning: str,
                 model_sha256: str) -> dict:
    if not isinstance(model, Pipeline) or list(model.named_steps) != ["tfidf", "classifier"]:
        raise ValueError("Expected PatchProbe pipeline")
    features = model.named_steps["tfidf"]
    classifier = model.named_steps["classifier"]
    if not isinstance(features, FeatureUnion) or not isinstance(classifier, LogisticRegression):
        raise ValueError("Expected FeatureUnion and LogisticRegression")
    branches = dict(features.transformer_list)
    if set(branches) != {"word", "char"}:
        raise ValueError("Unexpected feature branches")
    word = branches["word"]
    char = branches["char"]
    if word.analyzer != "word" or word.ngram_range != (1, 2) or not word.sublinear_tf:
        raise ValueError("Unexpected word vectorizer")
    if char.analyzer != "char_wb" or char.ngram_range != (3, 5) or not char.sublinear_tf:
        raise ValueError("Unexpected character vectorizer")
    if classifier.coef_.shape[1] != len(word.vocabulary_) + len(char.vocabulary_):
        raise ValueError("Feature count differs from classifier coefficients")
    if not np.isfinite(classifier.coef_).all() or not np.isfinite(classifier.intercept_).all():
        raise ValueError("Non-finite classifier weights")
    return {
        "formatVersion": 1,
        "model": {
            "version": version,
            "sha256": model_sha256,
            "trainedOn": trained_on,
            "warning": warning,
        },
        "classes": classifier.classes_.tolist(),
        "word": _vectorizer_payload(word),
        "char": _vectorizer_payload(char),
        "classifier": {
            "coef": classifier.coef_.tolist(),
            "intercept": classifier.intercept_.tolist(),
        },
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", type=Path, default=root / "artifacts/model/serving/model.joblib")
    parser.add_argument("--output", type=Path, default=root / "portal/src/lib/model.generated.json")
    parser.add_argument("--version", default="full-corpus-v1")
    parser.add_argument("--trained-on", default="531 human-confirmed Django release-note labels")
    parser.add_argument("--warning", default="Review suggestion only. Scores are uncalibrated; cross-project reliability is unproven.")
    args = parser.parse_args()
    digest = hashlib.sha256(args.model.read_bytes()).hexdigest()
    model = joblib.load(args.model)
    payload = export_model(model, version=args.version, trained_on=args.trained_on,
                           warning=args.warning, model_sha256=digest)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "classes": payload["classes"],
                      "features": len(payload["word"]["idf"]) + len(payload["char"]["idf"]),
                      "model_sha256": digest}, indent=2))


if __name__ == "__main__":
    main()
