import re


def extract_score(text):
    match = re.search(r"Trust Score:\s*(\d+)", text)

    if match:
        return int(match.group(1))

    return 50


def extract_risk(text):
    match = re.search(
        r"Risk Level:\s*(Low|Medium|High)",
        text,
        re.IGNORECASE,
    )

    if match:
        return match.group(1).title()

    return "Unknown"