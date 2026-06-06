from pathlib import Path
from unittest import result

from torch import chunk

from app.blueprints.chat_routes import chunks
from app.utils import faiss_manager
from app.utils.pdf_processor import PDFProcessor
from app.utils.csv_processor import CSVProcessor
from app.utils.web_scraper import WebScraper
from app.utils.chunk_processor import ChunkProcessor
from app.utils.logger import logger
from app.services.session_service import SessionService
from app.services.embedding_service import (EmbeddingService)
from app.services.vector_store import (vector_store)
from app.utils.faiss_manager import (FAISSManager)


class DocumentService:

    def __init__(self):
        self.pdf_processor = PDFProcessor()
        self.csv_processor = CSVProcessor()
        self.web_scraper = WebScraper()
        self.chunk_processor = ChunkProcessor()
        self.embedding_service = (EmbeddingService())

    def process_document(self, uploaded_file):

        extension = Path(
            uploaded_file.filename
        ).suffix.lower()

        if extension == ".pdf":

            upload_folder = Path(
                "uploads/pdfs"
            )

        elif extension == ".csv":

            upload_folder = Path(
                "uploads/csvs"
            )

        else:

            raise ValueError(
                "Unsupported file type"
            )

        upload_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            upload_folder /
            uploaded_file.filename
        )

        uploaded_file.save(file_path)

        logger.info(
            f"Uploaded file: {file_path}"
        )

        if extension == ".pdf":

            result = self.pdf_processor.extract_text(
                file_path
            )
            
            chunks = self.chunk_processor.create_chunks(result)

            embeddings = (
                self.embedding_service
                .create_embeddings(chunks)
            )

            dimension = len(
                embeddings[0]
            )

            faiss_manager = (FAISSManager(dimension))

            faiss_manager.add_vectors(embeddings)

            vector_store.set_chunks(chunks)

            vector_store.set_faiss_manager(faiss_manager)

            logger.info(f"Stored {len(chunks)} chunks in VectorStore")

        elif extension == ".csv":

            result = self.csv_processor.summarize_csv(file_path)

            csv_metadata = f"""
                CSV Dataset

            Rows: {result['rows']}
            Columns: {result['columns']}

            Column Names:
            {', '.join(result['column_names'])}
"""

            data_chunks = self.chunk_processor.create_chunks(
                result["full_text"]
            )

            chunks = []

            for chunk in data_chunks:
                chunks.append(
                csv_metadata + "\n\n" + chunk
        )

            embeddings = (
                self.embedding_service
                .create_embeddings(chunks)
            )

            dimension = len(embeddings[0])

            faiss_manager = FAISSManager(dimension)

            faiss_manager.add_vectors(embeddings)

            vector_store.set_chunks(chunks)

            logger.info(f"CSV Chunks Stored: {len(chunks)}")
            logger.info(f"First CSV Chunk:\n{chunks[0][:500]}")

            vector_store.set_faiss_manager(faiss_manager)

            logger.info(
                f"Stored {len(chunks)} CSV chunks in VectorStore"
            )

        else:

            raise ValueError(
                "Unsupported file type"
            )
        
        SessionService.set_value(
            "current_document",
            {
            "file_name": uploaded_file.filename,
            "file_type": extension
            }
        )

        logger.info(
            f"Successfully processed: {uploaded_file.filename}"
        )

        return {
            "file_path": str(file_path),
            "result": result,
            "file_type": extension
        }

    def process_website(self, url):

        result = self.web_scraper.extract_text(url)

        text = result["text"]

        chunks = (
            self.chunk_processor
            .create_chunks(text)
        )

        embeddings = (
            self.embedding_service
            .create_embeddings(chunks)
        )

        dimension = len(embeddings[0])

        faiss_manager = (FAISSManager(dimension))

        faiss_manager.add_vectors(embeddings)

        vector_store.set_chunks(chunks)

        vector_store.set_faiss_manager(faiss_manager)

        SessionService.set_value(
            "current_document",
            {
                "file_name": url,
                "file_type": "website"
            }
        )

        logger.info(
            f"Stored {len(chunks)} website chunks in VectorStore"
        )

        return result