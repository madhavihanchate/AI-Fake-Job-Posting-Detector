import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load local .env
load_dotenv()

# Try Streamlit Cloud secrets first
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
    API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"