import fitz  # PyMuPDF


def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF file uploaded through Streamlit.

    Args:
        uploaded_file: Streamlit UploadedFile object

    Returns:
        str: Extracted text
    """

    text = ""

    try:
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")

        for page in pdf:
            text += page.get_text()

        pdf.close()

    except Exception as e:
        print("Error:", e)

    return text