from app.services.embedding_service import (
    EmbeddingService
)

from app.utils import faiss_manager
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

    print(
        f"Embedding Dimension: {dimension}"
    )

    print(
        f"Vectors Stored: {faiss_manager.total_vectors()}"
    )

    query = (
    "How are users matched?"
    )

    query_embedding = (
        embedding_service.create_embedding(query)
    )

    distances, indices = (
        faiss_manager.search(
        query_embedding,
        top_k=2
        )
    )

    print(f"Indices: {indices}")

    print(f"Distances: {distances}")


if __name__ == "__main__":
    main()