from datetime import datetime

DATE_FORMATS = [
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S",
    "%d/%m/%Y",
    "%d/%m/%Y %H:%M:%S",
    "%m/%d/%Y",
    "%m/%d/%Y %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S"
]

INT_MIN = -2147483648
INT_MAX = 2147483647


def python_to_java_date_format(py_format: str) -> str:
    mapping = {
        "%Y": "yyyy",
        "%m": "MM",
        "%d": "dd",
        "%H": "HH",
        "%M": "mm",
        "%S": "ss",
        "T" : "'T'"
     }

    java_format = py_format

    for py_token, java_token in mapping.items():
        java_format = java_format.replace(py_token, java_token)

    return java_format




def detect_type(value):
    value = value.strip()

    # Boolean
    if value.lower() in ("true", "false"):
        return "id_Boolean"

    # Integer / Long
    try:
        n = int(value)

        if INT_MIN <= n <= INT_MAX:
            return "id_Integer"
        else:
            return "id_Long"
    except ValueError:
        pass

    # Float / Double
    try:
        f = float(value)

        # Choix personnel :
        # tout nombre décimal est considéré comme Double
        return "id_Double"
    except ValueError:
        pass

    # Date
    for fmt in DATE_FORMATS:
        try:
            datetime.strptime(value, fmt)
            return f"id_Date||{python_to_java_date_format(fmt)}"
        except ValueError:
            pass

    # String
    return "id_String"