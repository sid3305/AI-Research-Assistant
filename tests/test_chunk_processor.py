from app.utils.chunk_processor import ChunkProcessor


def main():

    sample_text = """
AI is changing healthcare.

Machine learning helps diagnosis.

Deep learning improves image analysis.
"""

    processor = ChunkProcessor()

    chunks = processor.create_chunks(
        sample_text
    )

    print("\nChunks:\n")

    for index, chunk in enumerate(
        chunks,
        start=1
    ):
        print(
            f"Chunk {index}:"
        )
        print(chunk)
        print("-" * 40)

    print(
        f"\nTotal Chunks: {len(chunks)}"
    )


if __name__ == "__main__":
    main()