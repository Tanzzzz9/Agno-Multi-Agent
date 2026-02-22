import os
from pypdf import PdfReader
from doc_store import store_document

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

def handle_upload(file):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    if file.filename.lower().endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
        if not text:
            raise ValueError("No text could be extracted from the PDF.")
        store_document(file.filename, text)
    else:
        raise ValueError("Only PDF files are supported.")
