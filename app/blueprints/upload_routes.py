from flask import Blueprint, request
from flask import render_template
from app.services.document_service import DocumentService
from flask import (
    Blueprint,
    request,
    render_template
)

upload_bp = Blueprint(
    "upload",
    __name__
)


@upload_bp.route("/")
def home():
    return render_template("index.html")
    
@upload_bp.route("/upload", methods=["POST"])
def upload_pdf():

    uploaded_file = request.files.get("pdf_file")

    if not uploaded_file:
        return "No file uploaded", 400
    
    allowed_extensions = (".pdf", ".csv")

    if not uploaded_file.filename.lower().endswith(
        allowed_extensions
    ):
        return (
            "Only PDF and CSV files are allowed",
            400
        )

    service = DocumentService()

    result = service.process_document(
    uploaded_file
    )

    if result["file_type"] == ".pdf":

        return f"""
        <h3>PDF Uploaded Successfully</h3>

        <pre>
        {result["result"][:3000]}
        </pre>
        """

    elif result["file_type"] == ".csv":

        summary = result["result"]

        return f"""
        <h3>CSV Uploaded Successfully</h3>

        <p><b>Rows:</b> {summary["rows"]}</p>

        <p><b>Columns:</b> {summary["columns"]}</p>

        <p><b>Column Names:</b></p>

        <pre>
        {summary["column_names"]}
        </pre>

        <h4>Preview</h4>

        <pre>
        {summary["preview"]}
        </pre>
        """
    else:
        return "Unsupported file type", 400
    
@upload_bp.route("/scrape", methods=["GET"])

def scrape_page():

    return """
    <h2>Scrape Website</h2>

    <form method="POST" action="/scrape">

        <input
            type="text"
            name="url"
            placeholder="https://example.com"
            size="50"
        >

        <button type="submit">
            Scrape
        </button>

    </form>
    """
@upload_bp.route("/scrape", methods=["POST"])
def scrape_website():

    url = request.form.get("url")

    if not url:
        return "No URL provided", 400

    service = DocumentService()

    try:
        result = service.process_website(url)

    except Exception as e:
        return str(e), 400

    return f"""
    <h3>{result['title']}</h3>

    <pre>
    {result['text'][:5000]}
    </pre>
    """

    