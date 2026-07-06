# Telco Customer Churn Predictor 📊🤖

An end-to-end Machine Learning project that identifies customer risk profiles and predicts the likelihood of telecom customer churn. This repository includes exploratory data analysis, feature engineering, model serialization, and a responsive cloud-deployed web dashboard.

🚀 **[View Live Web App](https://telco-customer-churn-prediction2676.streamlit.app/)**

---

## 📌 Project Overview
Customer churn directly impacts a company's bottom-line revenue. This project leverages data-driven insights to analyze patterns in customer behavior and predict attrition before it happens. By deploying an intuitive user interface, business stakeholders can test real customer scenarios on the fly to optimize retention strategies.

## 🛠️ Tech Stack
* **Core Language:** Python
* **Data Engineering & Visualization:** Pandas, NumPy, Seaborn, Matplotlib
* **Machine Learning Framework:** Scikit-Learn (Random Forest Classifier)
* **Production Deployment:** Streamlit Cloud, Git, GitHub

---

## 📈 Model Performance & Architecture
The predictive core utilizes a **Random Forest Classifier** trained and validated on processed customer account data.

* **Overall Accuracy:** 79%
* **Precision (Churn Class):** 0.63 (When the model flags a customer as a churn risk, it is correct 63% of the time)
* **Recall (Churn Class):** 0.48 (The model successfully isolates 48% of all true churners present in the evaluation pool)

### 🔑 Top 5 Feature Importances
The model relies heavily on financial metrics and commitment length to evaluate user risk:
1. **Total Charges** (19.3%)
2. **Monthly Charges** (16.9%)
3. **Tenure** (16.7%)
4. **Internet Service: Fiber Optic** (4.0%)
5. **Payment Method: Electronic Check** (3.5%)

### 💡 Operational Business Insights
* **High-Attrition Traps:** Exploratory analysis highlights that **Fiber Optic Internet** and **Electronic Check Payment Methods** carry the highest positive correlation with customer churn. 
* **Retention Drivers:** Customer tenure acts as the most dominant stabilizer against attrition; operational focus should target bolstering customer relationship programs during early lifecycle stages.

---

## 📁 Repository Structure
```text
├── App/
│   ├── app.py          # Production script for the Streamlit web app
│   └── model.pkl       # Serialized production-ready Random Forest model
├── Data/               # Raw and clean data footprints
├── Notebooks/
│   └── 01_exploration.ipynb  # Iterative exploration, EDA, and model evaluation logs
├── .gitignore          # Cache and environment isolation rules
└── requirements.txt    # Production environment dependency declaration