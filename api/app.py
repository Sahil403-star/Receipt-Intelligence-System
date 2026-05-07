from flask import Flask, request, jsonify

from receipt_parser.regex_parser import extract_receipt_data
from receipt_parser.ocr_cleaner import clean_ocr
from receipt_parser.fallback_engine import apply_fallback

from database.db import save_receipt

app = Flask(__name__)

@app.route("/parse_receipt", methods=["POST"])
def parse_receipt():

    text = request.json.get("text")

    cleaned = clean_ocr(text)

    data = extract_receipt_data(cleaned)

    data = apply_fallback(data)

    save_receipt(data)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)