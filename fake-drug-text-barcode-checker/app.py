import streamlit as st
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))

from predict import predict

st.set_page_config(page_title="Fake Drug Text/Barcode Checker", page_icon="💊", layout="centered")

st.title("💊 Fake Drug Text/Barcode Checker")
st.caption("NextGen Capstone Project — ML screening prototype")

st.warning(
    "IMPORTANT: This is an educational prototype trained on synthetic demonstration data. "
    "It cannot confirm that a medicine is genuine or counterfeit. Verify products through "
    "official NAFDAC channels and qualified professionals."
)

with st.form("checker"):
    drug_name = st.text_input("Product / Drug name", placeholder="e.g. DEMO Paracetamol 500mg")
    nafdac_number = st.text_input("NAFDAC registration number", placeholder="e.g. A11-1234")
    manufacturer = st.text_input("Manufacturer", placeholder="e.g. Demo Pharma Nigeria Ltd")
    batch_number = st.text_input("Batch number", placeholder="e.g. B12345")
    barcode = st.text_input("Barcode", placeholder="e.g. 1234567890123")
    submitted = st.form_submit_button("CHECK PRODUCT", use_container_width=True)

if submitted:
    record = {
        "drug_name": drug_name,
        "nafdac_number": nafdac_number,
        "manufacturer": manufacturer,
        "batch_number": batch_number,
        "barcode": barcode,
    }
    result = predict(record)

    if result["label"] == "suspicious":
        st.error(result["headline"])
    else:
        st.success(result["headline"])

    st.write(result["explanation"])
    st.metric("Prototype suspicious score", f"{result['suspicious_probability']:.1%}")

    st.subheader("Why it was flagged / checked")
    for reason in result["format_checks"]:
        st.write("• " + reason)

    st.info(
        "Next step: verify the product using official NAFDAC resources. "
        "Do not use this prototype as a substitute for regulatory verification."
    )

st.divider()
st.subheader("Official verification")
st.markdown(
    "NAFDAC's Greenbook is the official registered-product database: "
    "[greenbook.nafdac.gov.ng](https://greenbook.nafdac.gov.ng/)"
)
