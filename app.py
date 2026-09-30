import streamlit as st
import pickle

st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

with open("crop_model.pkl", "rb") as file:
    dt = pickle.load(file)

st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and environmental values to get a suitable crop recommendation.")

st.divider()

st.subheader("Soil & Environmental Conditions")

col1, col2 = st.columns(2)
with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=140.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=145.0)
    K = st.number_input("Potassium (K)", min_value=0.0, max_value=205.0)
    temperature = st.number_input("Temperature (°C)", min_value=8.0, max_value=44.0)

with col2:
    humidity = st.number_input("Humidity (%)", min_value=14.0, max_value=100.0)
    ph = st.number_input("pH", min_value=3.5, max_value=10.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=20.0, max_value=300.0)

st.divider()

col1, col2 = st.columns(2)

with col1:

    
    if st.button("Predict Crop", use_container_width=True):
        new_data = [[N, P, K, temperature, humidity, ph, rainfall]]
        prediction = dt.predict(new_data)
        st.success("Recommended Crop: " + prediction[0])
        st.write("This recommendation is based on the soil and environmental values entered.")

with col2:
    if st.button("Reset",use_container_width=True):
        st.session_state.N = 0.0
        st.session_state.P = 0.0
        st.session_state.K = 0.0
        st.session_state.temperature = 8.0
        st.session_state.humidity = 14.0
        st.session_state.ph = 3.5
        st.session_state.rainfall = 20.0
        st.rerun()

st.divider()

st.caption("Crop recommendation based on soil and environmental conditions.")