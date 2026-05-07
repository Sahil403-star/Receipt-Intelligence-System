def clean_ocr(text):
    replacements = {
        "O": "0",
        "l": "1",
        "S": "5"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text