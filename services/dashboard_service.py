from rag.vector_store import VectorStore


class DashboardService:

    @staticmethod
    def get_dashboard_data():

        vector_store = VectorStore()

        results = vector_store.collection.get()

        documents = results.get("documents", [])
        metadatas = results.get("metadatas", [])

        filenames = sorted(
            list(
                set(
                    metadata["filename"]
                    for metadata in metadatas
                )
            )
        )

        return {

            "total_documents": len(filenames),

            "total_chunks": len(documents),

            "total_embeddings": len(documents),

            "uploaded_files": filenames

        }