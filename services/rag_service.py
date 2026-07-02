from agents.pdf_agent import PDFAgent
from rag.text_splitter import TextSplitter
from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore


class RAGService:

    @staticmethod
    def process_document(filepath, filename):

        print("=" * 60)
        print("Processing:", filename)

        # Extract text
        extracted_text = PDFAgent.extract_text(filepath)

        # Split into chunks
        chunks = TextSplitter.split(extracted_text)

        print(f"Chunks Created: {len(chunks)}")

        # Generate embeddings
        embedding_model = EmbeddingModel()
        embeddings = embedding_model.encode(chunks)

        print("Embeddings Generated")

        # Store in ChromaDB
        vector_store = VectorStore()

        # Check for duplicate document
        if vector_store.document_exists(filename):

            print(f"{filename} already exists in ChromaDB.")

            return {
                "text": extracted_text,
                "chunks": chunks,
                "document_id": None,
                "already_exists": True
            }

        # Store new document
        document_id = vector_store.add_documents(
            chunks,
            embeddings,
            filename
        )

        print("Stored in ChromaDB")
        print("=" * 60)

        return {
            "text": extracted_text,
            "chunks": chunks,
            "document_id": document_id,
            "already_exists": False
        }