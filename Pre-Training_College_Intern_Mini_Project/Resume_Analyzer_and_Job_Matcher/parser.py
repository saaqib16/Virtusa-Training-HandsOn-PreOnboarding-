from os import PathLike

from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_source):
    if isinstance(pdf_source, (str, bytes, PathLike)):
        with open(pdf_source, "rb") as file:
            return _read_pdf_text(file)

    if hasattr(pdf_source, "seek"):
        pdf_source.seek(0)

    return _read_pdf_text(pdf_source)


def _read_pdf_text(file_obj):
    reader = PdfReader(file_obj)
    text_parts = []

    for page in reader.pages:
        text_parts.append(page.extract_text() or "")

    return " ".join(text_parts).lower()
