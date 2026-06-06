from app.services.embedding_service import (
    EmbeddingService
)

from app.services.vector_store import (
    vector_store
)


class RetrieverAgent:
    """
    Responsible for retrieving
    relevant chunks for each task.
    """

    def __init__(self):

        self.embedding_service = (
            EmbeddingService()
        )

    def retrieve(
        self,
        tasks,
        top_k=3
    ):

        chunks = (
            vector_store.get_chunks()
        )

        faiss_manager = (
            vector_store.get_faiss_manager()
        )

        if not chunks:

            raise ValueError(
                "No document loaded."
            )

        if not faiss_manager:

            raise ValueError(
                "No vector index available."
            )

        evidence = {}

        for task in tasks:

            query_embedding = (
                self.embedding_service
                .create_embedding(task)
            )

            distances, indices = (
                faiss_manager.search(
                    query_embedding,
                    top_k
                )
            )

            relevant_chunks = []

            for index in indices[0]:

                if (
                    index >= 0
                    and index < len(chunks)
                ):

                    relevant_chunks.append(
                        chunks[index]
                    )

            evidence[task] = (
                relevant_chunks
            )
        for task, chunks_found in evidence.items():
            print(f"\nTASK: {task}")
            print(f"RETRIEVED CHUNKS: {len(chunks_found)}")

            if chunks_found:
                print(f"FIRST CHUNK:\n{chunks_found[0][:500]}")
        return evidence