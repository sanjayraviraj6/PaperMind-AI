from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class RetrieverService:

    def __init__(self):

        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore()

    def search(self, query, top_k=5):

        embedding = self.embedding_model.encode(query)[0]

        return self.vector_store.search(
            embedding,
            top_k
        )

    def get_all_chunks(self):

        results = self.vector_store.collection.get()

        return results["documents"]