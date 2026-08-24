import streamlit as st
from google import genai


api_key = st.secrets["GEMINI_API_KEY"]

client = genai.Client(
    api_key=api_key
)

response = client.models.generate_content(
    model="gemini-3.7-flash",
    contents="Say hello to MediKiosk in one sentence."
)

print(response.text)