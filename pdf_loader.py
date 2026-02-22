from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import pytesseract

def load_pdf_text(file_path):
    text = ""

    # Try text extraction
    reader = PdfReader(file_path)
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    # Fallback to OCR
    if not text.strip():
        print("⚠️ Using OCR fallback")
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img) + "\n"

    return text.strip()
