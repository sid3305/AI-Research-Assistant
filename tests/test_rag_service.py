from app.services.rag_service import RAGService


def main():

    chunks = [
        "AI is changing healthcare.",
        "Machine learning helps diagnosis.",
        "Deep learning improves image analysis."
    ]

    question = (
        "What is machine learning?"
    )

    rag_service = RAGService()

    relevant_chunks = (
        rag_service.retrieve_relevant_chunks(
            question,
            chunks
        )
    )

    context = (
        rag_service.build_context(
            relevant_chunks
        )
    )

    print("\nRelevant Chunks:\n")

    for chunk in relevant_chunks:
        print(chunk)

    print("\nContext:\n")
    print(context)


if __name__ == "__main__":
    main()