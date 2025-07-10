# Patient No-Show Prediction and Revenue Loss Estimator

## Project Overview

Hospitals and clinics lose significant revenue and operational efficiency when patients miss scheduled appointments.  
This project aims to:

1. Predict patient no-shows using supervised machine learning.
2. Estimate potential revenue loss due to missed consultations.
3. Provide actionable insights for overbooking strategies and patient communication.

---

## Dataset Summary

Synthetic dataset with 1000 patient appointment records, including:

| Feature              | Description                                         |
|----------------------|-----------------------------------------------------|
| Appointment_ID       | Unique appointment identifier                       |
| Patient_ID           | Unique patient identifier                           |
| Age                  | Patient's age                                       |
| Gender               | Male/Female                                         |
| Scheduled_Day        | Date when appointment was scheduled                 |
| Appointment_Day      | Date of actual appointment                          |
| SMS_Sent             | Whether a reminder SMS was sent (0/1)               |
| Chronic_Conditions   | Patient has chronic disease (e.g., diabetes)        |
| Missed_Appointment   | Target variable: 1 = No-show, 0 = Showed up         |
| Consultation_Cost    | Cost charged per appointment (for revenue impact)   |

---

## Tools and Libraries Used

- Python 3
- Pandas, NumPy
- Scikit-learn (Random Forest Classifier)
- Matplotlib, Seaborn
- OpenPyXL (for Excel export)

---

## Problem Statement

Can we predict in advance if a patient is likely to miss their appointment and calculate how much revenue the hospital might lose if they don’t show up?

---

## Methodology Summary

1. Data Preprocessing
   - Convert date columns
   - Derive Days_Waited feature
   - Encode gender and drop unnecessary columns

2. Modeling
   - Train/test split
   - Fit a Random Forest Classifier
   - Evaluate using ROC-AUC, Confusion Matrix, and Classification Report

3. Revenue Impact Estimation
   - Multiply predicted no-show probability by consultation cost
   - Export to Excel for business reporting

---

## Sample Output

| Patient_ID | Predicted Probability | Consultation Cost | Expected Revenue Loss |
|------------|------------------------|-------------------|------------------------|
| P001       | 0.78                   | 1200              | 936                    |
| P002       | 0.15                   | 800               | 120                    |

---



