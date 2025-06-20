import streamlit as st

st.set_page_config(page_title="Game Theory Formulator", layout="centered")

st.title("🎮 Game Theory Problem → Math Formulation")

st.markdown("Enter a verbal description of a game theory problem:")

user_input = st.text_area("Problem Description", height=200)

if st.button("Generate Formulation"):
    st.markdown("You typed:")
    st.write(user_input)
