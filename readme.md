# 💼 Employee Salary Prediction Web App

This project is a machine learning-based web application that predicts employee salaries based on various input features such as education, experience, job title, location, age, and gender.

Built using **Python, scikit-learn, and Streamlit**, this app allows users to interactively estimate salaries by inputting values through a simple UI.

---


## 📦 Features

- Predict salary based on 6 fields:
  - Education
  - Experience
  - Location
  - Job Title
  - Age
  - Gender
- Model trained using Linear Regression
- Real-time prediction with a Streamlit frontend

---

## 🧠 Machine Learning Model

- **Preprocessing**:
  - Removed "High School" entries
  - One-hot encoding for categorical variables
  - Feature scaling for numeric columns
- **Model**: Linear Regression from `scikit-learn`
- **Evaluation**:
  - RMSE and R² used to validate performance

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas & NumPy
- Scikit-learn
- Streamlit
- Pickle (for model serialization)

---



