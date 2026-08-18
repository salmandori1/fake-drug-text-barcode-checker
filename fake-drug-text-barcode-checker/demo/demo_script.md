# 2–3 Minute Demo Video Script

## 0:00–0:25 — Introduction
Hello, my name is [YOUR NAME]. My NextGen capstone project is called **Fake Drug Text/Barcode Checker**.

The goal is to explore how machine learning can screen drug-product information and flag entries that may require further verification.

## 0:25–0:50 — Problem
Counterfeit and falsified medicines can endanger patients. My prototype focuses on product information such as the drug name, NAFDAC registration number, manufacturer, batch number and barcode.

## 0:50–1:15 — Technology
I built the prototype with Python, pandas, scikit-learn and Streamlit.

The machine-learning component uses TF-IDF text and character features with logistic regression. I also added basic formatting checks for identifiers.

## 1:15–2:00 — Live demonstration
Enter a synthetic demonstration product:

Drug name:
DEMO Paracetamol 500mg

NAFDAC number:
A11-1234

Manufacturer:
Demo Pharma Nigeria Ltd

Batch:
B12345

Barcode:
1234567890123

Click CHECK PRODUCT.

Show the result and explanation.

Then deliberately enter a malformed demonstration record, for example:

NAFDAC number:
FAKE-0001

Barcode:
ABC123

Batch:
B

Click CHECK PRODUCT again and show the suspicious result.

## 2:00–2:25 — Evaluation
Show the notebook evaluation metrics and confusion matrix.

Explain that the results come from synthetic demonstration data, so they do not represent real-world counterfeit-detection performance.

## 2:25–2:45 — Conclusion
This project demonstrates how machine learning can be used as a screening layer, while authoritative regulatory verification remains necessary.

For a future version, I would connect the application to an appropriately governed NAFDAC verification source and add validated barcode scanning.

Thank you.
