
import streamlit as st
import pandas as pd
from AIapi import EVAIAssistant
from model_utils import load_model, predict_range

st.set_page_config(page_title="EV Range Advisor", layout="wide")

st.title("EV Range Advisor")
st.write("Predict electric vehicle range using machine learning.")

# Load the saved model and AI assistant
@st.cache_resource
def get_model():
    return load_model()

try:
    model = get_model()
    model_error = None
except Exception as e:
    model = None
    model_error = str(e)

assistant = EVAIAssistant()

if model_error:
    st.error(f"Could not load the ML model: {model_error}")

col1, col2 = st.columns([1, 1.3])

with col1:
    st.subheader("Vehicle Specifications")

    with st.form("vehicle_form"):
        accel = st.number_input(
            "Acceleration (0–100 km/h, seconds)",
            min_value=1.0, max_value=30.0, value=7.0
        )

        top_speed = st.number_input(
            "Top speed (km/h)",
            min_value=50, max_value=400, value=180
        )

        efficiency = st.number_input(
            "Efficiency (Wh/km)",
            min_value=50, max_value=1000, value=180
        )

        fast_charge = st.number_input(
            "Fast charging speed (km/h)",
            min_value=0, max_value=2000, value=500
        )

        rapid_charge = st.selectbox(
            "Rapid charging supported",
            ["Yes", "No"]
        )

        powertrain = st.selectbox(
            "Powertrain", ["AWD", "RWD", "FWD"]
        )

        plug_type = st.selectbox(
            "Plug type",
            ["Type 2 CCS", "Type 2", "Type 2 CHAdeMO",
             "Type 1 CHAdeMO", "Type 1 CCS"]
        )

        body_style = st.selectbox(
            "Body style",
            ["SUV", "Sedan", "Hatchback", "Liftback",
             "Pickup", "Cabrio", "SPV", "Station"]
        )

        segment = st.selectbox(
            "Vehicle segment",
            ["A", "B", "C", "D", "E", "F", "N", "S"]
        )

        seats = st.number_input(
            "Number of seats",
            min_value=1, max_value=9, value=5
        )

        price = st.number_input(
            "Vehicle price (EUR)",
            min_value=1000, max_value=500000, value=35000
        )

        daily_km = st.number_input(
            "Daily driving distance (km)",
            min_value=1.0, max_value=1000.0, value=30.0
        )

        make = st.text_input("Vehicle brand", value="Generic")
        model_name = st.text_input("Vehicle model", value="EV")

        submitted = st.form_submit_button("Predict Range")

    if submitted:
        if model is None:
            st.error("The ML model is unavailable. Check the model file.")
        else:
            features = {
                "AccelSec": accel,
                "TopSpeed_KmH": top_speed,
                "Efficiency_WhKm": efficiency,
                "FastCharge_KmH": fast_charge,
                "RapidCharge": rapid_charge,
                "PowerTrain": powertrain,
                "PlugType": plug_type,
                "BodyStyle": body_style,
                "Segment": segment,
                "Seats": seats,
                "PriceEuro": price
            }

            try:
                pred_km = predict_range(features, model=model)

                if pred_km <= 0:
                    st.warning("The model returned a non-positive range.")
                else:
                    st.success(f"Predicted EV range: {pred_km:.1f} km")
                    st.write(
                        f"Estimated days between charges: "
                        f"{pred_km / daily_km:.1f}"
                    )

                    with st.expander("AI Insights"):
                        vehicle = {
                            "make": make,
                            "model": model_name,
                            "efficiency": efficiency,
                            "daily_km": daily_km
                        }

                        st.write("### Recommendation")
                        st.write(
                            assistant.recommend_vehicle(vehicle, pred_km)
                        )

                        st.write("### Maintenance Tips")
                        st.write(
                            assistant.maintenance_tips(
                                {"battery": "Refer to vehicle specifications"}
                            )
                        )

                        st.write("### Charging Strategy")
                        st.write(
                            assistant.charging_strategy(daily_km, pred_km)
                        )

            except Exception as e:
                st.error(f"Prediction failed: {e}")

with col2:
    st.subheader("AI Chat Assistant")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_msg = st.text_input("Ask anything about electric vehicles")

    if st.button("Send"):
        if user_msg.strip():
            try:
                reply = assistant.generate_text(user_msg)
            except Exception:
                reply = assistant._fallback(user_msg)

            st.session_state.chat_history.append(
                {"user": user_msg, "assistant": reply}
            )
        else:
            st.warning("Please enter a message.")

    for chat in reversed(st.session_state.chat_history):
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Assistant:** {chat['assistant']}")
        st.divider()
