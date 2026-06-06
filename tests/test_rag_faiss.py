from app.services.embedding_service import (
    EmbeddingService
)

from app.services.rag_service import (
    RAGService
)

from app.utils.faiss_manager import (
    FAISSManager
)


def main():

    chunks = [
        "Artificial Intelligence helps healthcare.",
        "Machine learning improves diagnosis.",
        "FastAPI is a backend framework."
    ]

    embedding_service = (
        EmbeddingService()
    )

    embeddings = (
        embedding_service.create_embeddings(
            chunks
        )
    )

    dimension = len(
        embeddings[0]
    )

    faiss_manager = (
        FAISSManager(
            dimension
        )
    )

    faiss_manager.add_vectors(
        embeddings
    )

    rag_service = (
        RAGService()
    )

    question = (
        "How does AI help medicine?"
    )

    relevant_chunks = (
        rag_service.retrieve_relevant_chunks(
            question,
            chunks,
            faiss_manager
        )
    )

    context = (
        rag_service.build_context(
            relevant_chunks
        )
    )

    print(
        "\nRelevant Chunks:\n"
    )

    for chunk in relevant_chunks:

        print(chunk)

    print(
        "\nContext:\n"
    )

    print(context)


if __name__ == "__main__":
    main()