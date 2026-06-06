from app.utils.pdf_processor import PDFProcessor


processor = PDFProcessor()

text = processor.extract_text("Friend Matchmaking.pdf")

print(text[:1000])