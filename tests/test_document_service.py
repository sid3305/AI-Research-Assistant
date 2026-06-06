from pathlib import Path

from app.utils.pdf_processor import PDFProcessor


class DocumentService:

    def __init__(self):
        self.pdf_processor = PDFProcessor()

    def process_document(self, uploaded_file):

        upload_folder = Path("uploads")

        upload_folder.mkdir(exist_ok=True)

        file_path = upload_folder / uploaded_file.filename

        uploaded_file.save(file_path)

        extracted_text = self.pdf_processor.extract_text(
            file_path
        )

        return {
            "file_path": str(file_path),
            "text": extracted_text
        }