import uuid
import chromadb
from datetime import datetime


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="papers"
        )

    def add_documents(
        self,
        chunks,
        embeddings,
        filename
    ):

        document_id = str(uuid.uuid4())

        ids = []
        metadatas = []

        for index in range(len(chunks)):

            ids.append(str(uuid.uuid4()))

            metadatas.append(
                {
                    "document_id": document_id,
                    "filename": filename,
                    "chunk_number": index + 1,
                    "uploaded_at": datetime.now().isoformat()
                }
            )

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

        return document_id

    def search(
        self,
        query_embedding,
        top_k=5,
        filename=None
    ):

        kwargs = {
            "query_embeddings": [query_embedding.tolist()],
            "n_results": top_k
        }

        if filename:
            kwargs["where"] = {
                "filename": filename
            }

        results = self.collection.query(**kwargs)

        if results.get("documents") and len(results["documents"]) > 0:
            return results["documents"][0]

        return []

    def get_top_chunks(self, limit=10):

        results = self.collection.get()

        documents = results.get("documents", [])

        if not documents:
            return []

        if len(documents) <= limit:
            return documents

        step = max(1, len(documents) // limit)

        selected_chunks = []

        for i in range(0, len(documents), step):

            selected_chunks.append(documents[i])

            if len(selected_chunks) == limit:
                break

        return selected_chunks

    def document_exists(self, filename):

        results = self.collection.get(
            where={
                "filename": filename
            }
        )

        documents = results.get("documents", [])

        return len(documents) > 0

    def get_document_chunks(self, filename):

        results = self.collection.get(
            where={
                "filename": filename
            }
        )

        return results

    def delete_document(self, filename):

        results = self.collection.get(
            where={
                "filename": filename
            }
        )

        ids = results.get("ids", [])

        if ids:
            self.collection.delete(ids=ids)

        return len(ids)