import re

def extract_receipt_data(text):
    data = {}

    total_match = re.search(r"TOTAL\s*\$?(\d+\.\d+)", text)

    date_match = re.search(r"(\d{2}/\d{2}/\d{4})", text)

    store_match = re.search(r"STORE:\s*(.*)", text)

    data["store"] = store_match.group(1) if store_match else "Unknown"

    data["date"] = date_match.group(1) if date_match else None

    data["total"] = float(total_match.group(1)) if total_match else None

    return data