import fitz
import pytesseract

from PIL import Image
from pdf2image import convert_from_bytes


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from both:
    1. Text-based PDFs
    2. Image-based (scanned) PDFs using OCR
    """

    pdf_bytes = uploaded_file.read()

    text = ""

    try:
        pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

        for page in pdf:
            text += page.get_text()

        pdf.close()

        # If normal extraction worked
        if text.strip():
            return text

        print("No text found. Switching to OCR...")

        images = convert_from_bytes(pdf_bytes)

        ocr_text = ""

        for image in images:
            ocr_text += pytesseract.image_to_string(image)

        return ocr_text

    except Exception as e:
        print("Parser Error:", e)
        return None