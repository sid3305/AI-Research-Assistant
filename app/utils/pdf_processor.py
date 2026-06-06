from pathlib import Path
import pdfplumber


class PDFProcessor:
    """
    Handles PDF text extraction.
    """

    def extract_text(self, pdf_path):
        """
        Extract text from a PDF file.

        Args:
            pdf_path (str or Path): Path to PDF file

        Returns:
            str: Extracted text
        """

        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"PDF file not found: {pdf_path}"
            )

        extracted_text = ""

        try:
            with pdfplumber.open(pdf_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        extracted_text += page_text + "\n"

            return extracted_text

        except Exception as e:
            raise RuntimeError(
                f"Failed to extract text from PDF: {e}"
        )