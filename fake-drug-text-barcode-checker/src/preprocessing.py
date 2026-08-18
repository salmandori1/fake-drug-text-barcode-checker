import re
import pandas as pd

NAFDAC_PATTERNS = [
    re.compile(r"^A11-\d{4,6}$", re.I),
    re.compile(r"^A4-\d{4,6}$", re.I),
    re.compile(r"^04-\d{4,6}$", re.I),
]

def normalize_text(value):
    return str(value or "").strip()

def check_format(value, patterns):
    value = normalize_text(value)
    return any(p.fullmatch(value) for p in patterns)

def barcode_is_plausible(barcode):
    s = normalize_text(barcode)
    return s.isdigit() and len(s) in {12, 13, 14}

def basic_checks(record):
    reasons = []
    nafdac = normalize_text(record.get("nafdac_number"))
    barcode = normalize_text(record.get("barcode"))
    batch = normalize_text(record.get("batch_number"))
    name = normalize_text(record.get("drug_name"))

    if not check_format(nafdac, NAFDAC_PATTERNS):
        reasons.append("NAFDAC number format is unusual for this prototype.")
    if not barcode_is_plausible(barcode):
        reasons.append("Barcode format is unusual or incomplete.")
    if len(batch) < 3:
        reasons.append("Batch number is missing or unusually short.")
    if len(name) < 4:
        reasons.append("Product name is missing or unusually short.")

    if not reasons:
        reasons.append("The supplied fields pass the prototype's basic formatting checks.")

    return reasons
