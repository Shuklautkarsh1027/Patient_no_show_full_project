


# Step 1: Import Libraries
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
```

---

#  Step 2: Load Dataset
```python
df = pd.read_csv("patient_appointments_large.csv")
df.head()
```

---

#  Step 3: Preprocess Data
```python
df['Scheduled_Day'] = pd.to_datetime(df['Scheduled_Day'])
df['Appointment_Day'] = pd.to_datetime(df['Appointment_Day'])
df['Days_Waited'] = (df['Appointment_Day'] - df['Scheduled_Day']).dt.days
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

# Drop unneeded columns
df_model = df.drop(['Appointment_ID', 'Patient_ID', 'Scheduled_Day', 'Appointment_Day'], axis=1)

# Define features and target
X = df_model.drop(['Missed_Appointment'], axis=1)
y = df_model['Missed_Appointment']
```

---

# Step 4: Train/Test Split
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

---

# Step 5: Model Training (Random Forest)
```python
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

# Step 6: Evaluation
```python
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, model.predict_proba(X_test)[:, 1]))
```

---

# Step 7: Revenue Loss Estimation
```python
X_test['Predicted_Prob'] = model.predict_proba(X_test)[:, 1]
X_test['Consultation_Cost'] = df_model.loc[X_test.index, 'Consultation_Cost']
X_test['Expected_Loss'] = X_test['Predicted_Prob'] * X_test['Consultation_Cost']
X_test[['Predicted_Prob', 'Consultation_Cost', 'Expected_Loss']].head()
```

---

#  Step 8: Save Output
```python
X_test[['Predicted_Prob', 'Consultation_Cost', 'Expected_Loss']].to_excel("revenue_loss_summary.xlsx", index=False)
```
