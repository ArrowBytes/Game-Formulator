import streamlit as st
from openai_backend import get_formulation

st.set_page_config(page_title="Game Theory Formulator", layout="centered")
st.title("🎮 Game Theory Problem → Math Formulation")

st.markdown("Enter a verbal description of a game theory problem:")

user_input = st.text_area("Problem Description", height=200)

if st.button("Generate Formulation"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            result = get_formulation(user_input)
            st.markdown("### 📘 Mathematical Formulation")
            st.markdown(result)
    else:
        st.warning("⚠️ Please enter a problem description.")
