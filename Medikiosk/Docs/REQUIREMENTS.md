# MediKiosk — Requirements

## 1. Project Objective

MediKiosk must allow patients to independently provide structured medical history, upload previous medical documents, and generate a physician-readable clinical summary before consultation.

---

# 2. Functional Requirements

## FR-01 — Language Selection

The system must allow the patient to select:

- Hindi
- English

---

## FR-02 — Consent

The system must:

- Explain the purpose of data collection
- Allow audio/text explanation
- Record patient consent
- End the session if consent is rejected

---

## FR-03 — Patient Registration

The system must collect:

- Name
- Age
- Gender
- Preferred language
- Optional demo ABHA ID

---

## FR-04 — Chief Complaint

The system must allow the patient to provide their chief complaint using:

- Voice
- Touch selection

The MVP must support:

- Chest pain
- Fever
- Cough
- Headache
- Abdominal pain
- Other

---

## FR-05 — Adaptive History

The system must select questions based on the patient's chief complaint.

Example:

Chest pain → chest pain questions.

Fever → fever-related questions.

The patient must be able to answer using:

- Voice
- Touch

---

## FR-06 — Structured History

The system must convert patient responses into structured fields such as:

- Chief complaint
- Onset
- Duration
- Location
- Severity
- Associated symptoms
- Past medical history
- Past surgical history
- Medications
- Allergies
- Family history
- Personal history

---

## FR-07 — Red-Flag Detection

The system must identify predefined combinations of potentially serious symptoms.

Example:

Chest pain + breathlessness + sweating

The system must:

- Mark the patient as high priority
- Display an alert
- Show the alert on the doctor dashboard

The system must NOT claim to diagnose the patient.

---

## FR-08 — Document Upload

The system must allow patients to upload:

- Prescriptions
- Lab reports
- Discharge summaries

Supported MVP formats:

- JPG
- PNG
- PDF

---

## FR-09 — OCR

The system must extract text from uploaded documents.

The system should identify:

- Medication names
- Dosages
- Investigation names
- Investigation values
- Dates
- Diagnoses when identifiable

---

## FR-10 — Medical Timeline

The system must organize extracted medical events chronologically.

---

## FR-11 — AI Summary

The system must generate a structured clinical summary containing:

- Chief complaint
- History of present illness
- Past medical history
- Past surgical history
- Medications
- Allergies
- Family history
- Personal history
- Relevant investigations
- Red flags

---

## FR-12 — Doctor Dashboard

The doctor dashboard must show:

- Patient queue
- Patient priority
- Chief complaint
- Red-flag status

---

## FR-13 — Doctor Review

The doctor must be able to:

- View the complete history
- View original documents
- Edit AI-generated information
- Confirm the final summary

---

# 3. AI Requirements

## AI-01 — Speech-to-Text

The system should convert patient speech into text.

MVP languages:

- Hindi
- English

---

## AI-02 — Clinical Information Extraction

The system should identify relevant medical information from patient responses.

Example:

"Seene mein do ghante se dard hai."

→

Chest pain = true  
Duration = 2 hours

---

## AI-03 — Adaptive Questioning

The system should select relevant questions based on the patient's responses.

---

## AI-04 — Summary Generation

The system should generate a structured summary from:

- Patient responses
- Extracted document information
- Medical timeline

---

# 4. Safety Requirements

## SAF-01

AI-generated information must be clearly marked as a draft.

## SAF-02

The system must not autonomously diagnose diseases.

## SAF-03

The system must not autonomously prescribe medicines.

## SAF-04

Red-flag alerts must recommend immediate clinical assessment rather than diagnosis.

## SAF-05

Doctors must be able to verify and modify AI-generated information.

---

# 5. User Experience Requirements

The system should be usable by:

- Elderly users
- Low-literacy users
- First-time users

The interface should provide:

- Large buttons
- Simple language
- Icons
- Audio instructions
- Voice input
- Touch input
- Minimal typing

---

# 6. Data Requirements

The system should store:

### Patient

- Patient ID
- Name
- Age
- Gender
- Language

### History

- Questions
- Answers
- Structured clinical fields

### Documents

- Document type
- Upload date
- OCR text
- Extracted medical information

### Summary

- AI-generated summary
- Doctor-edited summary
- Confirmation status

### Consent

- Consent status
- Timestamp

---

# 7. Technical Requirements

## Frontend

React-based web application.

## Backend

Python + FastAPI.

## Database

PostgreSQL.

## AI

Python-based AI services.

## OCR

OCR engine for medical documents.

## API

REST APIs between frontend and backend.

---

# 8. MVP Limitations

The prototype will NOT include:

- Real Aadhaar authentication
- Real ABHA integration
- Real hospital HIS integration
- Production FHIR integration
- Autonomous diagnosis
- Autonomous treatment recommendation
- Full regional-language support
- Production-grade handwritten medical OCR
- Physical kiosk hardware

These features are considered future development/integration scope.

---

# 9. Success Criteria

The MVP will be considered successful if:

1. A patient can complete a complete intake session.
2. The patient can answer questions through voice or touch.
3. The system can identify the chief complaint.
4. The system can detect predefined red flags.
5. The patient can upload a medical document.
6. The system can extract useful information from the document.
7. The system can generate a structured clinical summary.
8. The summary appears on the doctor dashboard.
9. The doctor can edit and confirm the summary.
10. The complete patient-to-doctor workflow works end-to-end.