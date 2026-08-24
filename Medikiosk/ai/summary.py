from google import genai
import streamlit as st


def generate_clinical_summary(
    patient,
    complaint,
    history,
    red_flags
):
    """
    Generate a physician-readable clinical summary
    using Gemini.

    This is a documentation assistant.
    It does not diagnose or prescribe.
    """

    api_key = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are assisting with clinical documentation.

Create a concise, structured clinical history from
the information provided below.

IMPORTANT RULES:
- Do NOT diagnose the patient.
- Do NOT recommend treatment.
- Do NOT prescribe medication.
- Do NOT invent information.
- Only use information provided below.
- Clearly mention information that is unavailable.
- Preserve the patient's reported information.
- This is a draft requiring physician verification.

PATIENT INFORMATION:
{patient}

CHIEF COMPLAINT:
{complaint}

STRUCTURED HISTORY:
{history}

RED FLAGS:
{red_flags}

Use these sections:

## CHIEF COMPLAINT

## HISTORY OF PRESENT ILLNESS

## RELEVANT ASSOCIATED SYMPTOMS

## PAST HISTORY

## MEDICATIONS / ALLERGIES

## CLINICAL PRIORITY

## PHYSICIAN VERIFICATION

Remember:
This is documentation assistance only.
Do not provide diagnosis or treatment.
"""

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text