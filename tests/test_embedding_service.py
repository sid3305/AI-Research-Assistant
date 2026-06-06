from app.services.embedding_service import (
    EmbeddingService
)


def main():

    service = EmbeddingService()

    text = (
        "Artificial Intelligence is transforming healthcare."
    )

    embedding = (
        service.create_embedding(text)
    )

    print(
        f"Embedding Dimension: {len(embedding)}"
    )

    print(
        embedding[:10]
    )


if __name__ == "__main__":
    main()