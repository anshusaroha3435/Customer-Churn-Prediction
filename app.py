# Gender -> 1 Female 0 Male
# Churn -> 1 Yes 0 No
# Scaler is exported as scaler.pkl
# Model is exported as model.pkl
# Order of the X -> 'Age', 'Tenure', 'MonthlyCharges', 'Gender'

import joblib
import pandas as pd
import numpy as np
import streamlit as st

scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

st.title("Churn Prediction App")

st.divider()

st.write("please enter the following details to predict whether the customer will churn or not")

st.divider()

age = st.number_input("Enter Age", min_value=10, max_value=100, value=30)

tenure = st.number_input("Enter Tenure", min_value=0, max_value=130, value=10)

monthly_charges = st.number_input("Enter Monthly Charges", min_value=30, max_value=150, value=70)   

gender = st.selectbox("Select Gender",["Male", "Female"])

st.divider()

predictbutton = st.button("Predict!")

st.divider()

if predictbutton:
    gender_selected = 1 if gender == "Female" else 0
    X = [age, tenure, monthly_charges, gender_selected]
    X1 = np.array(X)
    X_array = scaler.transform([X1])
    prediction = model.predict(X_array)[0]

    predicted = "Churn" if prediction == 1 else "Not Churn"

    st.balloons()

    st.write(f"Predicted : {predicted}")
else:
    st.write("Please enter the details and click on Predict button to get the prediction")