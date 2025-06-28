# Employee Attrition Prediction Using Data Science
This project aims to develop a predictive model that identifies employees at risk of leaving their jobs (attrition) based on personal, professional, and organizational factors. The objective is to help companies retain valuable talent through proactive HR strategies driven by data.

----

## 1. Project Overview
Employee attrition is a major concern for organizations, leading to high recruitment costs and productivity loss. Using data science techniques, this project aims to:

- Identify key factors contributing to employee attrition

- Build machine learning models to predict whether an employee is likely to leave

- Provide actionable insights for employee engagement and retention strategies

----

## 2. Dataset Description
Source: Kaggle

The dataset includes a wide variety of features categorized into:

- Personal Information:
Age, Gender, Marital Status, Number of Dependents

- Compensation & Benefits:
Monthly Income, Number of Promotions, Remote Work

- Work Environment & Engagement:
Work-Life Balance, Job Satisfaction, Performance Rating, Overtime, Leadership Opportunities, Innovation Opportunities, Employee Recognition

- Other Factors:
Distance from Home, Education Level, Company Reputation

- Target Variable:
Attrition: Binary classification — Stayed or Left

----

## 4. Data Preprocessing

- Missing Values: No missing values detected

- Duplicated Values: No duplicated values detected

- Categorical Encoding: Applied Label Encoding to convert categorical features

----

## 5. Model Development
Multiple machine learning models were tested. XGBoost was selected as the final model due to its:

- High accuracy

- Robust performance on imbalanced data

- Capability to capture both linear and non-linear patterns

- Built-in support for feature importance analysis

The final XGBoost model was saved and prepared for deployment.

----

## 6. Model Deployment
Input Features:

- Job Level

- Marital Status

- Remote Work

- Work-Life Balance

- Gender

- Number of Promotions

- Company Reputation

- Education Level

- Number of Dependents

- Overtime

- Job Satisfaction

- Distance from Home

----

## 7. Challenges Faced
- Data Collection: Time-consuming and required extensive search

- Outliers: Retained Monthly Income outliers for data distribution integrity

- Feature Selection for Plots: Needed to avoid noisy or uninformative visuals

- Text Data: Required appropriate encoding without losing semantics

-----

## 8. Key Insights
- Top Predictors of Attrition: Overtime, Job Satisfaction, Age, and Years at Company

- Explainable ML: Feature importance helped HR understand what drives attrition

- Business Value: Early prediction helps prevent costly employee turnover

- Balanced Metrics: Focused on F1-score and ROC-AUC, not just accuracy

----

## 9. Integration Recommendations
- HR Dashboards: Embed predictions into HR dashboards for continuous monitoring

- Clinical Decision Support: Show risk scores + suggested actions

- Decision Support: Use predictions to prioritize employee engagement programs

- Alerts & Follow-ups: Automatically alert HR when a high-risk employee is detected

- Feedback Mechanism: Continuous learning from new data over time

- Policy Development: Tailor HR policies based on insights from the model

----

## 10. Tools & Technologies

| Category         | Tools                         |
| ---------------- | ----------------------------- |
| Language         | Python                        |
| Data Processing  | pandas, NumPy                 |
| Machine Learning | scikit-learn, XGBoost         |
| Visualization    | Matplotlib, Seaborn, Power BI |

----

## 11. Project Structure
Health-Care-Project/

│

├── APP/                           # App-related files (possibly UI or interface)

│

├── CODE/                          # Final scripts and source code

│

├── DATASETS/                      # Processed datasets

│

├── DEPLOYMENT/                    # Deployment logic or configuration

│

├── Dashboard/                     # Power BI dashboards and reports

│

├── REPORTS/                       # Final reports and documentation

│

├── README.md                      # Project documentation and overview

│

├── requirements.txt               # List of required Python packages

