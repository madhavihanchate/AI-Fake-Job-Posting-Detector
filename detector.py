import re

SCAM_PATTERNS = {
    "Registration Fee": r"registration fee|processing fee|pay.*fee",
    "Training Fee": r"training fee|security deposit",
    "WhatsApp Only": r"whatsapp",
    "Personal Email": r"gmail\.com|yahoo\.com|hotmail\.com",
    "Immediate Joining": r"immediate joining|join today|urgent hiring",
    "Guaranteed Job": r"100% job|guaranteed placement",
    "Huge Salary": r"\₹?\s?\d{1,3},?\d{3,}\s*/?\s*month",
}

def detect_red_flags(text):

    detected = []

    for name, pattern in SCAM_PATTERNS.items():

        if re.search(pattern, text, re.IGNORECASE):
            detected.append(name)

    return detected