# utils/red_flags.py


def detect_red_flags(complaint, history):
    """
    Detect predefined red-flag combinations.

    This is NOT a diagnosis system.
    It only identifies symptoms requiring
    priority clinical review.
    """

    flags = []

    # -----------------------------------------
    # CHEST PAIN
    # -----------------------------------------

    if complaint == "Chest Pain":

        breathlessness = history.get("breathlessness") == "Yes"
        sweating = history.get("sweating") == "Yes"
        radiation = history.get("radiation")

        if breathlessness and sweating:

            flags.append({
                "severity": "HIGH",
                "message": (
                    "Chest pain with breathlessness "
                    "and sweating requires immediate "
                    "clinical assessment."
                )
            })

        elif breathlessness:

            flags.append({
                "severity": "HIGH",
                "message": (
                    "Chest pain with difficulty breathing "
                    "requires priority clinical assessment."
                )
            })

        elif radiation in [
            "Left arm",
            "Jaw",
            "Back"
        ]:

            flags.append({
                "severity": "HIGH",
                "message": (
                    "Chest pain with radiation to another "
                    "area requires priority clinical assessment."
                )
            })

        elif history.get("severity", 0) >= 8:

            flags.append({
                "severity": "HIGH",
                "message": (
                    "Severe chest pain requires "
                    "priority clinical assessment."
                )
            })


    # -----------------------------------------
    # FEVER
    # -----------------------------------------

    elif complaint == "Fever":

        chills = history.get("chills") == "Yes"

        if chills:

            flags.append({
                "severity": "MEDIUM",
                "message": (
                    "Fever with chills should be "
                    "reviewed by clinical staff."
                )
            })


    # -----------------------------------------
    # COUGH
    # -----------------------------------------

    elif complaint == "Cough":

        breathlessness = history.get("breathlessness") == "Yes"

        if breathlessness:

            flags.append({
                "severity": "HIGH",
                "message": (
                    "Cough with difficulty breathing "
                    "requires priority clinical assessment."
                )
            })


    # -----------------------------------------
    # HEADACHE
    # -----------------------------------------

    elif complaint == "Headache":

        severity = history.get("severity", 0)
        vomiting = history.get("vomiting") == "Yes"

        if severity >= 8 and vomiting:

            flags.append({
                "severity": "HIGH",
                "message": (
                    "Severe headache with vomiting "
                    "requires priority clinical assessment."
                )
            })


    return flags