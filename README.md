# Patient No-Show Prediction and Revenue Loss Estimator

## Overview
This project predicts if a patient will miss their appointment using Random Forest,
and estimates expected revenue loss for the hospital or clinic.

## Dataset Features
- Age, Gender, Scheduled & Appointment Days
- SMS Sent, Chronic Conditions
- Missed Appointment (Target)
- Consultation Cost

## Output
- Classification Report
- ROC AUC Score
- Expected Revenue Loss Report (.xlsx)

## Folder Structure
```
patient_no_show_full_project/
├── no_show_prediction.py
├── patient_appointments_large.csv
├── revenue_loss_summary.xlsx  (generated after running)
├── visuals/
└── README.md
```

## How to Run
1. Install Python packages: `pandas, numpy, matplotlib, seaborn, scikit-learn, openpyxl`
2. Run `no_show_prediction.py` or convert it to `.ipynb`
