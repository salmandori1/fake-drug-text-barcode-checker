from pathlib import Path
import joblib
from preprocessing import basic_checks

ROOT = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT / "model.joblib"

MODEL = joblib.load(MODEL_PATH)

def combine(record):
    cols = ["drug_name", "nafdac_number", "manufacturer", "batch_number", "barcode"]
    return " | ".join(str(record.get(c, "") or "") for c in cols)

def predict(record):
    text = combine(record)
    label = MODEL.predict([text])[0]
    probabilities = MODEL.predict_proba([text])[0]
    classes = list(MODEL.classes_)
    suspicious_probability = float(probabilities[classes.index("suspicious")])

    format_reasons = basic_checks(record)

    if label == "suspicious":
        headline = "SUSPICIOUS — VERIFY"
        explanation = (
            "The model detected patterns similar to the synthetic suspicious examples "
            "used for this capstone prototype."
        )
    else:
        headline = "LOOKS CONSISTENT — STILL VERIFY"
        explanation = (
            "The model did not detect a strong suspicious pattern in the supplied fields. "
            "This does not prove that the medicine is genuine."
        )

    return {
        "label": label,
        "headline": headline,
        "suspicious_probability": suspicious_probability,
        "explanation": explanation,
        "format_checks": format_reasons,
    }
