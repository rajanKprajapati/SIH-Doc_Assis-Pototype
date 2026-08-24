# MediKiosk — User Journey

## 1. Overview

MediKiosk allows a patient to provide their medical history through voice or touch, upload previous medical documents, and receive a structured clinical summary that can be reviewed by a doctor.

---

## 2. Patient Journey

### Step 1 — Start

Patient opens MediKiosk.

System displays:

- MediKiosk welcome screen
- Language selection

Patient selects:

- Hindi
- English

---

### Step 2 — Consent

System explains:

- What information will be collected
- Why it is being collected
- That the information will be shared with the doctor

Patient chooses:

- Agree
- Don't Agree

If patient doesn't agree:

→ Session ends.

If patient agrees:

→ Continue to patient information.

---

### Step 3 — Patient Information

Patient provides:

- Name
- Age
- Gender
- Preferred language
- ABHA ID (optional/demo)

System creates a patient/session record.

---

### Step 4 — Chief Complaint

System asks:

"What brings you to the hospital today?"

Patient can:

- Speak the answer
- Select from predefined complaints

Initial complaints supported by MVP:

- Chest pain
- Fever
- Cough
- Headache
- Abdominal pain
- Other

---

### Step 5 — Clinical History

Based on the chief complaint, MediKiosk selects an appropriate question flow.

Example:

Chest Pain →

- Onset
- Location
- Character
- Severity
- Radiation
- Aggravating factors
- Relieving factors
- Associated symptoms

Patient can answer using:

- Voice
- Touch

The system converts the answers into structured clinical information.

---

### Step 6 — Red-Flag Detection

The system checks collected symptoms against predefined red-flag rules.

Example:

Chest pain + breathlessness + sweating

→ Potential red flag.

System displays a priority warning and sends the patient to the priority queue.

The system does NOT provide a diagnosis.

---

### Step 7 — Medical Documents

Patient can upload:

- Prescription
- Laboratory report
- Discharge summary

System:

1. Receives document
2. Performs OCR
3. Extracts relevant information
4. Stores extracted information
5. Adds information to the medical timeline

Patient can skip this step.

---

### Step 8 — Clinical Summary

MediKiosk combines:

- Patient information
- Clinical history
- Previous medical documents
- Extracted medications
- Relevant investigations
- Red-flag information

The AI generates a structured clinical summary.

The summary is marked:

"AI-generated draft — physician verification required."

---

### Step 9 — Submit

Patient reviews the available information and submits the session.

The case is added to the doctor's queue.

---

# 3. Doctor Journey

### Step 10 — Doctor Dashboard

Doctor logs into MediKiosk.

Doctor sees:

- Patient queue
- Patient ID
- Chief complaint
- Priority status
- Red-flag indicator

Example:

🚨 P1024 — Chest Pain — HIGH PRIORITY

---

### Step 11 — Patient Case

Doctor opens a patient.

System displays:

- Patient information
- Chief complaint
- History of present illness
- Past medical history
- Medications
- Allergies
- Previous investigations
- Medical timeline
- Uploaded documents
- Red flags
- AI-generated summary

---

### Step 12 — Doctor Verification

Doctor can:

- Edit the summary
- Correct extracted information
- Review original documents
- Confirm the final history

The doctor remains responsible for the final clinical record.

---

### Step 13 — End

After confirmation:

Patient case is marked as:

CONFIRMED

The consultation can proceed.

---

# 4. Complete Journey

Patient
↓
Language
↓
Consent
↓
Patient Information
↓
Chief Complaint
↓
Adaptive History
↓
Voice / Touch
↓
Red-Flag Detection
↓
Document Upload
↓
OCR + Extraction
↓
AI Clinical Summary
↓
Submit
↓
Doctor Queue
↓
Doctor Review
↓
Edit / Confirm
↓
Consultation