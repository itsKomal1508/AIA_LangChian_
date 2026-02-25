import streamlit as st
from agent import optimize_prompt
from sheets import save_to_sheet

# -------------------- Page Config -------------------- #
st.set_page_config(
    page_title="Elite Prompt Agent",
    page_icon="🎯",
    layout="centered"
)

# -------------------- Header -------------------- #
st.title("🎯 Elite Prompt Engineering Agent")
st.markdown(
    "Turn messy ideas into **professional AI-ready prompts** instantly."
)

st.divider()

# -------------------- Input Section -------------------- #
user_input = st.text_area(
    "Enter your messy prompt:",
    height=150,
    placeholder="Example: i want to build an ai app but don't know how to start..."
)

# -------------------- Button Logic -------------------- #
if st.button("🚀 Optimize Prompt"):

    if not user_input.strip():
        st.warning("Please enter a prompt first.")
    
    else:
        try:
            with st.spinner("Optimizing your prompt..."):
                result = optimize_prompt(user_input)

            st.subheader("✨ Optimized Prompt")
            st.code(result)

            # Save to Google Sheets
            save_to_sheet(user_input, result)
            st.success("Saved to Google Sheet ✅")

        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.divider()

# -------------------- Footer -------------------- #
st.caption("Built with LangChain + Groq + Streamlit")