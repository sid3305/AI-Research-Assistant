from sentence_transformers import SentenceTransformer


class EmbeddingService:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            cls._model = SentenceTransformer(
                "all-MiniLM-L6-v2"
            )

        return cls._model

    def create_embedding(
        self,
        text
    ):

        model = self.get_model()

        return model.encode(
            text
        )

    def create_embeddings(
        self,
        texts
    ):

        model = self.get_model()

        return model.encode(
            texts
        )