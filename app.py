import streamlit as st
import numpy as np
import pickle  # Change joblib to pickle

# Load the trained model using pickle
with open('rainfall_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Set a custom title and header image
st.set_page_config(page_title="Rainfall Prediction", page_icon="🌧️", layout="wide")

# Streamlit app title with a new color theme (light blue)
st.markdown("<h1 style='text-align: center; color: #0077B6;'>Rainfall Prediction App</h1>", unsafe_allow_html=True)

# Instructions with updated text and new font color
st.markdown("""
    <div style='text-align: center; font-size: 18px; color: #333333;'>
        <p>This app predicts the rainfall level for a month based on the rainfall data from the last 3 months.</p>
        <p>Please input the rainfall levels for the last 3 months to predict the current month's rainfall.</p>
    </div>
""", unsafe_allow_html=True)

# Input fields with updated color theme (blue and white)
col1, col2, col3 = st.columns(3)

with col1:
    aug_rainfall = st.number_input('Enter rainfall for 3 months ago (in mm)', min_value=0.0, step=0.1, value=279.56)
with col2:
    sep_rainfall = st.number_input('Enter rainfall for 2 months ago (in mm)', min_value=0.0, step=0.1, value=628.70)
with col3:
    oct_rainfall = st.number_input('Enter rainfall for 1 month ago (in mm)', min_value=0.0, step=0.1, value=368.70)

# Add some space between inputs and the prediction button
st.markdown("<br><br>", unsafe_allow_html=True)

# Make prediction when the user submits the inputs
if st.button('Predict Rainfall', key="predict_button"):
    # Prepare the input for prediction
    input_features = np.array([[aug_rainfall, sep_rainfall, oct_rainfall]])

    # Make prediction
    predicted_rainfall = model.predict(input_features)

    # Display the predicted rainfall with a custom style (using blue)
    st.markdown(f"""
        <div style='text-align: center; font-size: 24px; font-weight: bold; color: #0077B6;'>
            Predicted rainfall for this month: {predicted_rainfall[0]:.2f} mm
        </div>
    """, unsafe_allow_html=True)

    # Display a related message based on the prediction
    if predicted_rainfall[0] > 300:
        st.markdown("<h3 style='text-align: center; color: #0077B6;'>Heavy rainfall expected!</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='text-align: center; color: #0077B6;'>Moderate rainfall expected.</h3>", unsafe_allow_html=True)

# Add CSS for sticky footer with new theme (light blue footer)
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #0077B6;
            color: white;
            text-align: center;
            padding: 10px;
        }
        button[aria-expanded="true"] {
            background-color: #0077B6 !important;
        }
        button[aria-expanded="false"] {
            background-color: #0077B6 !important;
        }
    </style>
    <div class="footer">
        Built with ❤️ by Your Karan Chhillar | Rainfall Prediction App
    </div>
""", unsafe_allow_html=True)
