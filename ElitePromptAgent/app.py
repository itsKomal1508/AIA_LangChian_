import streamlit as st
from agent import optimize_prompt
from sheets import save_to_sheet

st.set_page_config(page_title="Elite Prompt Agent", page_icon="🎯")

st.title("🎯 Elite Prompt Engineering Agent")
st.markdown("Turn messy ideas into professional AI-ready prompts.")

user_input = st.text_area("Enter your messy prompt")

if st.button("Optimize"):
    if user_input.strip() != "":

        with st.spinner("Optimizing your prompt..."):
            result = optimize_prompt(user_input)

        st.subheader("Optimized Prompt:")
        st.write(result)

        save_to_sheet(user_input, result)

        st.success("Saved to Google Sheet!")

    else:
        st.warning("Please enter a prompt first.")