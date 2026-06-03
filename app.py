import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("diabetes_model.pkl", "rb"))

st.title("Diabetes Prediction App")

Pregnancies = st.number_input("Pregnancies", min_value=0)
Glucose = st.number_input("Glucose", min_value=0)
BloodPressure = st.number_input("Blood Pressure", min_value=0)
SkinThickness = st.number_input("Skin Thickness", min_value=0)
Insulin = st.number_input("Insulin", min_value=0)
BMI = st.number_input("BMI", min_value=0.0)
DiabetesPedigreeFunction = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0
)
Age = st.number_input("Age", min_value=0)

if st.button("Predict"):

    input_data = pd.DataFrame({
        "Pregnancies":[Pregnancies],
        "Glucose":[Glucose],
        "BloodPressure":[BloodPressure],
        "SkinThickness":[SkinThickness],
        "Insulin":[Insulin],
        "BMI":[BMI],
        "DiabetesPedigreeFunction":[DiabetesPedigreeFunction],
        "Age":[Age]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Diabetic")
    else:
        st.success("Not Diabetic")