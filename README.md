# Customer Churn Prediction

A machine learning web application that predicts whether a customer is likely to **churn or stay** based on demographic and account-related information.

## Features

* Interactive **Streamlit** web interface.
* Takes customer **Age, Tenure, Monthly Charges, and Gender** as inputs.
* Uses a pre-trained machine learning model for churn prediction.
* Applies the same pre-trained scaler used during model training.
* Displays the prediction as **Churn** or **Not Churn**.

## Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit

## How It Works

1. Enter the customer's details.
2. The input features are converted into the required numerical format.
3. The saved scaler transforms the input data.
4. The trained ML model predicts whether the customer will churn.
5. The prediction is displayed through the Streamlit interface.

## Model Inputs

* Age
* Tenure
* Monthly Charges
* Gender

The model expects the features in this exact order: `Age`, `Tenure`, `MonthlyCharges`, `Gender`.

## Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

## Running Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL displayed in the terminal.
