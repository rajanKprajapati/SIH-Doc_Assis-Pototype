# ai/history_engine.py


HISTORY_FLOWS = {

    "Chest Pain": [

        {
            "id": "onset",
            "question": "When did the chest pain start?",
            "type": "text"
        },

        {
            "id": "location",
            "question": "Where exactly is the pain?",
            "type": "choice",
            "options": [
                "Center of chest",
                "Left side",
                "Right side",
                "Other"
            ]
        },

        {
            "id": "severity",
            "question": "How severe is the pain?",
            "type": "scale",
            "min": 0,
            "max": 10
        },

        {
            "id": "radiation",
            "question": "Does the pain move to another part of your body?",
            "type": "choice",
            "options": [
                "Left arm",
                "Right arm",
                "Back",
                "Jaw",
                "No"
            ]
        },

        {
            "id": "breathlessness",
            "question": "Are you having difficulty breathing?",
            "type": "yes_no"
        },

        {
            "id": "sweating",
            "question": "Are you experiencing unusual sweating?",
            "type": "yes_no"
        },

        {
            "id": "dizziness",
            "question": "Are you feeling dizzy or light-headed?",
            "type": "yes_no"
        },

        {
            "id": "nausea",
            "question": "Are you experiencing nausea or vomiting?",
            "type": "yes_no"
        }
    ],


    "Fever": [

        {
            "id": "duration",
            "question": "How long have you had the fever?",
            "type": "text"
        },

        {
            "id": "temperature",
            "question": "What was your highest recorded temperature?",
            "type": "text"
        },

        {
            "id": "chills",
            "question": "Are you experiencing chills?",
            "type": "yes_no"
        },

        {
            "id": "body_pain",
            "question": "Do you have body pain?",
            "type": "yes_no"
        }
    ],


    "Cough": [

        {
            "id": "duration",
            "question": "How long have you had the cough?",
            "type": "text"
        },

        {
            "id": "phlegm",
            "question": "Are you producing phlegm?",
            "type": "yes_no"
        },

        {
            "id": "breathlessness",
            "question": "Are you having difficulty breathing?",
            "type": "yes_no"
        }
    ],


    "Headache": [

        {
            "id": "duration",
            "question": "When did the headache start?",
            "type": "text"
        },

        {
            "id": "severity",
            "question": "How severe is the headache?",
            "type": "scale",
            "min": 0,
            "max": 10
        },

        {
            "id": "dizziness",
            "question": "Are you feeling dizzy?",
            "type": "yes_no"
        },

        {
            "id": "vomiting",
            "question": "Are you experiencing vomiting?",
            "type": "yes_no"
        }
    ],


    "Abdominal Pain": [

        {
            "id": "onset",
            "question": "When did the abdominal pain start?",
            "type": "text"
        },

        {
            "id": "location",
            "question": "Where is the pain located?",
            "type": "choice",
            "options": [
                "Upper abdomen",
                "Lower abdomen",
                "Left side",
                "Right side",
                "Around the navel",
                "Other"
            ]
        },

        {
            "id": "severity",
            "question": "How severe is the pain?",
            "type": "scale",
            "min": 0,
            "max": 10
        },

        {
            "id": "vomiting",
            "question": "Are you experiencing vomiting?",
            "type": "yes_no"
        },

        {
            "id": "diarrhea",
            "question": "Are you experiencing diarrhea?",
            "type": "yes_no"
        }
    ]
}


def get_questions(complaint):
    """Return questions for the selected complaint."""

    return HISTORY_FLOWS.get(complaint, [])