# Fake Drug Text/Barcode Checker

## NextGen Capstone Project

### Project title
**Fake Drug Text/Barcode Checker**

### Problem context
Counterfeit and falsified medicines are a serious public-health concern. This project explores a machine-learning screening approach for suspicious product information.

### What this MVP does
The prototype accepts:
- Product/drug name
- NAFDAC registration number
- Manufacturer
- Batch number
- Barcode

It then:
1. Runs a text/identifier ML classifier.
2. Performs simple formatting checks.
3. Returns a **SUSPICIOUS — VERIFY** or **LOOKS CONSISTENT — STILL VERIFY** result.
4. Explains the basic checks that contributed to the result.

### Safety / scope
**This is an educational capstone prototype, not a medicine-authentication service.**

The included dataset is synthetic. The model does not prove that a real medicine is genuine or counterfeit, and it must not be used to make medical or purchasing decisions.

For real-world verification, use authoritative NAFDAC resources. NAFDAC's Greenbook provides a registered-product database: https://greenbook.nafdac.gov.ng/

### Tech stack
- Python
- pandas
- scikit-learn
- Streamlit
- Google Colab / Jupyter
- joblib

### Repository structure

```text
fake-drug-text-barcode-checker/
├── data/
│   └── synthetic_drug_records.csv
├── notebooks/
│   └── fake_drug_checker.ipynb
├── src/
│   ├── preprocessing.py
│   └── predict.py
├── app.py
├── model.joblib
├── metrics.json
├── requirements.txt
├── README.md
└── demo/
    └── demo_script.md
```

### Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

### Model evaluation
The included model was trained and evaluated on a held-out portion of the **synthetic demonstration dataset**.

- Accuracy: 0.954
- Precision (suspicious): 1.000
- Recall (suspicious): 0.875
- F1 (suspicious): 0.933

These numbers are **not evidence of real-world performance** because the data is synthetic.

### Demo
See `demo/demo_script.md` for the 2–3 minute presentation script.

### Future improvements
1. Work with an appropriately governed, validated real-world dataset.
2. Connect to an authoritative product-registration/verification source.
3. Add camera barcode scanning.
4. Add stronger explainability.
5. Add audit logs and security controls.
6. Conduct independent validation before any real-world use.
