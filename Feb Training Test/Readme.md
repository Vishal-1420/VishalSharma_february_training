# Customer Churn Data Preprocessing

## 📌 Project Overview
This project performs complete data preprocessing on a Customer Churn dataset to prepare it for machine learning. All required preprocessing steps such as cleaning, encoding, scaling, outlier handling, and skewness transformation were implemented.

---

## 📊 Dataset Details
- Rows: 64,374  
- Features: 12  
- Target Variable: `Churn`  
- Categorical Features: Gender, Subscription Type, Contract Length  
- Numerical Features: Age, Tenure, Usage Frequency, Support Calls, Payment Delay, Total Spend, Last Interaction  

---

## 🧹 Data Preprocessing Steps

### ✔ Data Cleaning
- Removed irrelevant column (`CustomerID`)
- Verified data types
- No missing values found
- No duplicate records

### ✔ Outlier Treatment
- Used IQR method
- Treated outliers in `Total Spend`

### ✔ Categorical Encoding (separate file)
Implemented:
- One-Hot Encoding
- Label Encoding
- Ordinal Encoding
- Frequency Encoding
- Target Encoding

### ✔ Feature Scaling (separate file)
Applied:
- Min-Max Scaling
- Max Absolute Scaling
- Vector Normalization
- Standardization (Z-score)

Standardization was found most effective due to varying feature ranges.

### ✔ Skewness Transformation
- Log transformation applied to `Total Spend`
- Reduced positive skewness

### ✔ Train-Test Split
- 80% Training
- 20% Testing
- `random_state = 42`

---
