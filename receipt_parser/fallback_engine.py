def apply_fallback(data):
    if not data.get("store"):
        data["store"] = "Fallback Store"

    return data