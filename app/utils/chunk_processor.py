class ChunkProcessor:

    def create_chunks(
        self,
        text,
        chunk_size=500
    ):

        if not text:
            return []

        chunks = []

        for i in range(
            0,
            len(text),
            chunk_size
        ):

            chunk = text[
                i:i + chunk_size
            ]

            chunks.append(
                chunk.strip()
            )

        return chunks