from receipt_parser.regex_parser import extract_receipt_data
from receipt_parser.ocr_cleaner import clean_ocr

with open("receipts/sample_ocr.txt") as f:
    text = f.read()

cleaned = clean_ocr(text)

data = extract_receipt_data(cleaned)

print(data)