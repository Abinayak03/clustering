import streamlit as st
import pickle
import numpy as np

# Load your trained clustering model
with open("final_model.pkl", "rb") as f:   
    model = pickle.load(f)

st.title("Customer Spending Prediction App")

# User inputs
age = st.number_input("Enter Age", min_value=10, max_value=100, step=1)
income = st.number_input("Enter Annual Income (k$)",step=1)
score = st.number_input("Enter Spending Score (1-100)", min_value=1, max_value=100, step=1)
gender = st.selectbox("Select Gender", ("Male", "Female"))

# Encode gender (assuming 1=Male, 2=Female like in your dataset)
gender_val = 1 if gender == "Male" else 2

if st.button("Predict"):
    # Prepare input for model
    features = np.array([[age, income, score, gender_val]])
    
    # Predict cluster
    cluster = model.predict(features)[0]

    # Map cluster to spending type
    mapping = {
        0: "High Spending",
        1: "Low Spending",
        2: "Average Spending"
    }
    result = mapping.get(cluster, "Unknown")

    st.success(f"Cluster: {cluster} → {result}")