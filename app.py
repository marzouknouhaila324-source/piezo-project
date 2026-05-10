import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("best_model.pkl")

# Website title
st.title("Piezoelectric Energy Prediction")

# User inputs
voltage = st.number_input("Voltage")
current = st.number_input("Current")
weight = st.number_input("Weight")
step_loc = st.number_input("Step Location")

# Feature engineering
V_x_I = voltage * current
V_per_kg = voltage / weight if weight != 0 else 0

# Predict button
if st.button("Predict"):

    input_data = pd.DataFrame({
        'voltage(v)': [voltage],
        'current(uA)': [current],
        'weight(kgs)': [weight],
        'step_loc_enc': [step_loc],
        'V_x_I': [V_x_I],
        'V_per_kg': [V_per_kg]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Power: {prediction[0]:.4f} mW")