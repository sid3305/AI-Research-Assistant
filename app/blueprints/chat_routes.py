from flask import Blueprint
from flask import request

from app.services.session_service import SessionService
from app.services.rag_service import (
    RAGService
)

chat_bp = Blueprint(
    "chat",
    __name__
)


@chat_bp.route("/chat", methods=["GET"])
def chat_home():
    return "Chat Blueprint Working"


@chat_bp.route("/test-chat")
def test_chat():

    SessionService.add_chat_message(
        "What is AI?",
        "Artificial Intelligence"
    )

    return {
        "message": "Chat stored"
    }


@chat_bp.route("/history")
def history():

    return {
        "history":
        SessionService.get_chat_history()
    }


@chat_bp.route("/current-document")
def current_document():

    return {
        "document":
        SessionService.get_current_document()
    }


@chat_bp.route("/clear-session")
def clear_session():

    SessionService.clear_session()

    return {
        "message":
        "Session cleared"
    }

@chat_bp.route("/chunks")
def chunks():

    return {
        "chunks":
        SessionService.get_document_chunks()
    }
@chat_bp.route("/chunks")

@chat_bp.route("/vector-info")
def vector_info():

    from app.services.vector_store import (
        vector_store
    )

    chunks = (
        vector_store.get_chunks()
    )

    faiss_manager = (
        vector_store.get_faiss_manager()
    )

    return {
        "chunks": len(chunks),

        "vectors":
        faiss_manager.total_vectors()
        if faiss_manager
        else 0
    }

@chat_bp.route("/ask", methods=["POST"])
def ask_question():

    data = request.get_json()

    question = data.get("question")

    if not question:

        return {"error":"Question is required."}, 400

    try:

        rag_service = (RAGService())

        result = (rag_service.answer_question(question))

        SessionService.add_chat_message(
            question,
            result["answer"]
        )

        return {
            "question":result["question"],
            "answer":result["answer"]
        }

    except Exception as e:

        return {"error":str(e)}, 500
    
@chat_bp.route("/ask-test")
def ask_test():

    rag_service = (
        RAGService()
    )

    result = (
        rag_service.answer_question(
            "Summarize methodology and expected outcomes."
        )
    )

    return {
        "question":
        result["question"],

        "answer":
        result["answer"]
    }