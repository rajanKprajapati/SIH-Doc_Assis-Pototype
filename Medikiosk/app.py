import streamlit as st

from ai.history_engine import get_questions
from utils.red_flags import detect_red_flags


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MediKiosk",
    page_icon="🏥",
    layout="centered"
)


# =========================================================
# SESSION STATE
# =========================================================

if "step" not in st.session_state:
    st.session_state.step = 1

if "language" not in st.session_state:
    st.session_state.language = None

if "consent" not in st.session_state:
    st.session_state.consent = False

if "patient" not in st.session_state:
    st.session_state.patient = {}

if "chief_complaint" not in st.session_state:
    st.session_state.chief_complaint = None

if "history_answers" not in st.session_state:
    st.session_state.history_answers = {}

if "history_index" not in st.session_state:
    st.session_state.history_index = 0

if "red_flags" not in st.session_state:
    st.session_state.red_flags = []


# =========================================================
# HELPER
# =========================================================

def next_step():
    st.session_state.step += 1


# =========================================================
# HEADER
# =========================================================

st.title("🏥 MediKiosk")
st.caption("AI Clinical Intake Platform")

st.divider()


# =========================================================
# STEP 1 — WELCOME
# =========================================================

if st.session_state.step == 1:

    st.header("Welcome")

    st.write(
        "MediKiosk helps collect your medical history "
        "before you meet the doctor."
    )

    st.info(
        "You can answer questions using simple selections."
    )

    if st.button(
        "🚀 Start Patient Intake",
        use_container_width=True
    ):
        next_step()
        st.rerun()


# =========================================================
# STEP 2 — LANGUAGE
# =========================================================

elif st.session_state.step == 2:

    st.header("🌐 Select Language")

    language = st.radio(
        "Choose your preferred language:",
        ["English", "हिन्दी"]
    )

    if st.button(
        "Continue →",
        use_container_width=True
    ):
        st.session_state.language = language
        next_step()
        st.rerun()


# =========================================================
# STEP 3 — CONSENT
# =========================================================

elif st.session_state.step == 3:

    st.header("🔐 Consent")

    st.write(
        "MediKiosk will collect your health information "
        "to prepare your medical history for the doctor."
    )

    consent = st.checkbox(
        "I understand and agree to provide my information."
    )

    if st.button(
        "I Agree",
        disabled=not consent,
        use_container_width=True
    ):
        st.session_state.consent = True
        next_step()
        st.rerun()


# =========================================================
# STEP 4 — PATIENT DETAILS
# =========================================================

elif st.session_state.step == 4:

    st.header("👤 Patient Information")

    name = st.text_input("Full Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=25
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    abha_id = st.text_input(
        "ABHA ID (Optional — Demo Only)"
    )

    if st.button(
        "Continue →",
        use_container_width=True
    ):

        if not name.strip():

            st.warning("Please enter your name.")

        else:

            st.session_state.patient = {
                "name": name,
                "age": age,
                "gender": gender,
                "abha_id": abha_id
            }

            next_step()
            st.rerun()


# =========================================================
# STEP 5 — CHIEF COMPLAINT
# =========================================================

elif st.session_state.step == 5:

    st.header("🩺 What brings you to the hospital?")

    complaint = st.radio(
        "Select your main complaint:",
        [
            "Chest Pain",
            "Fever",
            "Cough",
            "Headache",
            "Abdominal Pain",
            "Other"
        ]
    )

    if st.button(
        "Continue to Medical History →",
        use_container_width=True
    ):

        st.session_state.chief_complaint = complaint

        next_step()
        st.rerun()


# =========================================================
# STEP 6 — READY
# =========================================================

elif st.session_state.step == 6:

    st.header("✅ Intake Started")

    st.success(
        "Your basic information has been recorded."
    )

    st.write("### Patient")

    st.write(
        f"**Name:** {st.session_state.patient['name']}"
    )

    st.write(
        f"**Age:** {st.session_state.patient['age']}"
    )

    st.write(
        f"**Gender:** {st.session_state.patient['gender']}"
    )

    st.write(
        f"**Main Complaint:** "
        f"{st.session_state.chief_complaint}"
    )

    st.divider()

    st.info(
        "The next step will ask questions "
        "about your medical problem."
    )

    if st.button(
        "Begin Medical History →",
        use_container_width=True
    ):

        st.session_state.step = 7
        st.rerun()


# =========================================================
# STEP 7 — CLINICAL HISTORY
# =========================================================

elif st.session_state.step == 7:

    st.header("🩺 Medical History")

    complaint = st.session_state.chief_complaint

    questions = get_questions(complaint)

    current_index = st.session_state.history_index


    # =====================================================
    # ALL QUESTIONS COMPLETED
    # =====================================================

    if current_index >= len(questions):

        st.success(
            "Clinical history completed."
        )

        st.write("### Structured History")

        st.json(
            st.session_state.history_answers
        )

        # ---------------------------------------------
        # RED FLAG DETECTION
        # ---------------------------------------------

        flags = detect_red_flags(
            complaint,
            st.session_state.history_answers
        )

        st.session_state.red_flags = flags

        st.divider()

        st.write("### 🚦 Clinical Priority Check")

        if flags:

            for flag in flags:

                if flag["severity"] == "HIGH":

                    st.error(
                        f"🚨 HIGH PRIORITY\n\n"
                        f"{flag['message']}"
                    )

                else:

                    st.warning(
                        f"⚠️ {flag['severity']} PRIORITY\n\n"
                        f"{flag['message']}"
                    )

        else:

            st.success(
                "No predefined red flags detected."
            )

        st.info(
            "This system does not provide a diagnosis. "
            "A qualified healthcare professional must "
            "evaluate the patient."
        )

        if st.button(
            "Continue →",
            use_container_width=True
        ):

            st.session_state.step = 8
            st.rerun()


    # =====================================================
    # ASK CURRENT QUESTION
    # =====================================================

    else:

        current_question = questions[current_index]

        progress = (
            (current_index + 1)
            / len(questions)
        )

        st.progress(progress)

        st.caption(
            f"Question {current_index + 1} "
            f"of {len(questions)}"
        )

        st.subheader(
            current_question["question"]
        )

        question_type = current_question["type"]


        # ---------------------------------------------
        # TEXT
        # ---------------------------------------------

        if question_type == "text":

            answer = st.text_input(
                "Your answer:",
                key=f"answer_{current_question['id']}"
            )


        # ---------------------------------------------
        # CHOICE
        # ---------------------------------------------

        elif question_type == "choice":

            answer = st.radio(
                "Select one:",
                current_question["options"],
                key=f"answer_{current_question['id']}"
            )


        # ---------------------------------------------
        # YES / NO
        # ---------------------------------------------

        elif question_type == "yes_no":

            answer = st.radio(
                "Select:",
                ["Yes", "No"],
                key=f"answer_{current_question['id']}"
            )


        # ---------------------------------------------
        # SCALE
        # ---------------------------------------------

        elif question_type == "scale":

            answer = st.slider(
                "Select severity:",
                current_question["min"],
                current_question["max"],
                5,
                key=f"answer_{current_question['id']}"
            )


        # ---------------------------------------------
        # NEXT
        # ---------------------------------------------

        if st.button(
            "Next →",
            use_container_width=True
        ):

            if (
                question_type == "text"
                and not answer.strip()
            ):

                st.warning(
                    "Please provide an answer."
                )

            else:

                st.session_state.history_answers[
                    current_question["id"]
                ] = answer

                st.session_state.history_index += 1

                st.rerun()


# =========================================================
# STEP 8 — TEMPORARY SUMMARY SCREEN
# =========================================================

elif st.session_state.step == 8:

    st.header("📋 Case Ready for Doctor")

    st.success(
        "Patient history has been collected successfully."
    )

    st.write("### Patient")

    st.write(
        f"**Name:** "
        f"{st.session_state.patient.get('name', '')}"
    )

    st.write(
        f"**Age:** "
        f"{st.session_state.patient.get('age', '')}"
    )

    st.write(
        f"**Complaint:** "
        f"{st.session_state.chief_complaint}"
    )

    st.write("### Clinical History")

    st.json(
        st.session_state.history_answers
    )

    if st.session_state.red_flags:

        st.write("### 🚨 Priority Alerts")

        for flag in st.session_state.red_flags:

            st.error(
                f"{flag['severity']}: "
                f"{flag['message']}"
            )

    else:

        st.success(
            "No predefined red flags detected."
        )

    st.divider()

    st.info(
        "AI physician summary will be added in Stage 6."
    )