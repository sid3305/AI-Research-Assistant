import faiss
import numpy as np


class FAISSManager:

    def __init__(
        self,
        dimension
    ):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(
            dimension
        )

    def add_vectors(
        self,
        vectors
    ):

        vectors = np.array(
            vectors,
            dtype=np.float32
        )

        self.index.add(
            vectors
        )

    def total_vectors(
        self
    ):

        return self.index.ntotal
    
    def search(self,query_vector,top_k=3):

        query_vector = np.array(
            [query_vector],
            dtype=np.float32
        )

        distances, indices = (
            self.index.search(
                query_vector,
                top_k
            )
        )

        return distances, indices