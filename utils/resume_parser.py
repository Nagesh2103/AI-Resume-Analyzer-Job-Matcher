import fitz
from docx import Document
def extract_text_from_pdf(file):
    """
    Extract text from a PDF file.
    """
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    pdf.close()
    return text

def extract_text_from_docx(file):
    """
    Extract text from a DOCX file.
    """
    document = Document(file)
    text = ""
    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"
    return text

def extract_text(file):
    """
    Detect file type and extract text.
    """
    file_name = file.name.lower()
    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif file_name.endswith("docx"):
        return extract_text_from_docx(file)
    else:
        raise ValueError(
            "Unsupported file format. Please upload PDF or DOCX."
        )
    