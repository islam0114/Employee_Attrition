import numpy as np
import streamlit as st
import pandas as pd
import pickle

Data = pickle.load(open('DEPLOYMENT/xgboost.sav', 'rb'))

st.set_page_config(page_title="Employee Attrition", page_icon="👤", layout="wide")
st.title("Employee Attrition Prediction App")
st.markdown('Predict whether an employee is attrition based on various attributes.')

# Input Form
st.markdown("---")
st.subheader("📝 Enter Employee Data:")

mapping_1 = {'Entry': 0, 'Mid': 1, "Senior": 2}
Job_Level_choice = st.selectbox('Job Level', list(mapping_1.keys()))
Job_Level = mapping_1[Job_Level_choice]

mapping_2 = {'Divorced': 0, 'Married': 1, "Single": 2}
Marital_Status_choice = st.selectbox('Marital Status', list(mapping_2.keys()))
Marital_Status = mapping_2[Marital_Status_choice]

mapping_3 = {'No': 0, 'Yes': 1}
Remote_Work_choice = st.selectbox('Remote Work', list(mapping_3.keys()))
Remote_Work = mapping_3[Remote_Work_choice]

mapping_4 = {'Excellent': 0, 'Fair': 1, "Good": 2,"Poor": 3}
Work_Life_Balance_choice = st.selectbox('Work-Life Balance', list(mapping_4.keys()))
Work_Life_Balance = mapping_4[Work_Life_Balance_choice]

mapping_5 = {'Female': 0, 'Male': 1}
Gender_choice = st.selectbox('Gender', list(mapping_5.keys()))
Gender = mapping_5[Gender_choice]

Number_of_Promotions = st.number_input("Number of Promotions (0 ==> 5)", min_value=0, max_value=5,step=1)


mapping_6 = {'Excellent': 0, 'Fair': 1, "Good": 2,"Poor": 3}
Company_Reputation_choice = st.selectbox('Company Reputation', list(mapping_6.keys()))
Company_Reputation = mapping_6[Company_Reputation_choice]

mapping_7 = {'Associate Degree': 0, 'Bachelor’s Degree': 1, "High School": 2,"Master’s Degree": 3,"PhD": 4}
Education_Level_choice = st.selectbox('Education Level', list(mapping_7.keys()))
Education_Level = mapping_7[Education_Level_choice]

Number_of_Dependents = st.number_input("Number of Dependents (0 ==> 10)", min_value=0, max_value=10,step=1)

mapping_8 = {'No': 0, 'Yes': 1}
Overtime_choice = st.selectbox('Overtime', list(mapping_8.keys()))
Overtime = mapping_8[Overtime_choice]

mapping_9 = {'High': 0, 'Low': 1, "Medium": 2,"Very High": 3}
Job_Satisfaction_choice = st.selectbox('Job Satisfaction', list(mapping_9.keys()))
Job_Satisfaction = mapping_9[Job_Satisfaction_choice]

Distance_from_Home = st.number_input("Distance from Home (0 ==> 100 km)", min_value=0, max_value=100,step=1)

df = pd.DataFrame({
    "Job Level": [Job_Level],
    "Marital Status": [Marital_Status],
    "Remote Work": [Remote_Work],
    "Work-Life Balance": [Work_Life_Balance],
    "Gender": [Gender],
    "Number of Promotions": [Number_of_Promotions],
    "Company Reputation": [Company_Reputation],
    "Education Level": [Education_Level],
    "Number of Dependents": [Number_of_Dependents],
    "Overtime": [Overtime],
    "Job Satisfaction": [Job_Satisfaction],
    "Distance from Home": [Distance_from_Home]
}, index=[0])

con = st.button("🔍 predict Attrition")
if con:
    result = Data.predict(df)
    if result == 1:
        st.write("The employee is likely to stay in the company")
    else:
        st.write("The employee is likely to leave the company")
