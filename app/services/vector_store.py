class VectorStore:

    def __init__(self):

        self.chunks = []

        self.faiss_manager = None

    def set_chunks(
        self,
        chunks
    ):

        self.chunks = chunks

    def get_chunks(self):

        return self.chunks

    def set_faiss_manager(
        self,
        faiss_manager
    ):

        self.faiss_manager = faiss_manager

    def get_faiss_manager(self):

        return self.faiss_manager
    
vector_store = VectorStore()