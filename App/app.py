import streamlit as st
import pandas as pd
import joblib
import os

# Get the absolute path of the directory where app.py lives
current_dir = os.path.dirname(os.path.abspath(__file__))
# Join that path with 'model.pkl'
model_path = os.path.join(current_dir, 'model.pkl')

# Load your trained model using the exact path
model = joblib.load(model_path)

st.title("Customer Churn Predictor")

# Create sliders for user input
tenure = st.slider('Tenure (months)', 0, 72, 12)
monthly_charges = st.number_input('Monthly Charges', 0.0, 200.0, 50.0)

# Button to predict
if st.button('Predict Churn'):
    # 1. Ask the model exactly what columns it expects to see
    expected_columns = model.feature_names_in_
    
    # 2. Create a blank DataFrame with 1 row, filling all expected columns with 0
    input_data = pd.DataFrame(0, index=[0], columns=expected_columns)
    
    # 3. Update only the columns we are collecting from our Streamlit sliders
    input_data['tenure'] = tenure
    input_data['MonthlyCharges'] = monthly_charges
    
    # 4. Make the prediction!
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("⚠️ High Churn Risk!")
    else:
        st.success("✅ Customer likely to stay.")