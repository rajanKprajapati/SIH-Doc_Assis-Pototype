import streamlit as st


st.set_page_config(
    page_title="MediKiosk",
    page_icon="🏥",
    layout="centered"
)


st.title("🏥 MediKiosk")

st.subheader("AI Clinical Intake Platform")

st.write(
    "A patient-friendly system for collecting clinical history "
    "and preparing a structured summary for doctors."
)

st.divider()

st.write("### Ready to begin?")

if st.button("🚀 Start Patient Intake", use_container_width=True):
    st.success("Patient intake started!")