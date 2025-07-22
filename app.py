import streamlit as st
import pandas as pd
import pickle

# Load trained model
with open("salary_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Salary Predictor", layout="centered")

st.title("💼 Employee Salary Predictor")
st.markdown("Predict an employee's salary based on their profile.")

# Input fields
education = st.selectbox("Education", ["Bachelor", "Master", "PhD"])
experience = st.slider("Years of Experience", 0, 40, 5)
location = st.selectbox("Location", ["Urban", "Suburban", "Rural"])
job_title = st.selectbox("Job Title", ["Manager", "Analyst", "Director"])
age = st.slider("Age", 18, 65, 30)
gender = st.selectbox("Gender", ["Male", "Female"])

# Prepare input
input_data = pd.DataFrame({
    "Education": [education],
    "Experience": [experience],
    "Location": [location],
    "Job_Title": [job_title],
    "Age": [age],
    "Gender": [gender]
})

# Predict
if st.button("Predict Salary 💰"):
    predicted_salary = model.predict(input_data)
    st.success(f"Estimated Salary: ₹{predicted_salary[0]:,.2f}")
