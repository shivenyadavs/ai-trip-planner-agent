import streamlit as st
from agent import plan_trip

st.set_page_config(page_title="AI Trip Planner Agent", layout="wide")

st.title("🌍 AI Trip Planner Agent")
st.write("Plan your trip using AI + Real-Time Weather Data")

user_input = st.text_input(
    "Enter your trip request:",
    "Plan a 3-day trip to Tokyo in May"
)

if st.button("Generate Trip Plan"):
    with st.spinner("Planning your trip..."):
        result = plan_trip(user_input)
        st.markdown(result)
