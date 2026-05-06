import streamlit as st
import google.generativeai as genai

# Page title
st.set_page_config(page_title="EGIP-Gemini Studio", page_icon="🎤")
st.title("🎤 EGIP-Gemini Studio")
st.subheader("සිංදු පද සහ නිර්මාණාත්මක අදහස් මෙතැනින්")

# Get API Key from Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("කරුණාකර Streamlit Secrets හි API Key එක ඇතුළත් කරන්න.")

# User Input
user_prompt = st.text_input("ඔබට අවශ්‍ය දේ මෙහි ලියන්න:", placeholder="උදා: සහෝදර බැඳීම ගැන සිංදුවක් ලියන්න")

if st.button("Generate"):
    if user_prompt:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(user_prompt)
            st.success("ඔබේ නිර්මාණය මෙන්න:")
            st.write(response.text)
        except Exception as e:
            st.error(f"දෝෂයක් ඇති විය: {e}")
    else:
        st.warning("කරුණාකර යමක් ටයිප් කරන්න.")

st.markdown("---")
st.caption("Developed by Indika Prabath")
