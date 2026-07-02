from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from services.groq_service import GroqService


class ChatService:

    @staticmethod
    def ask(question):

        print("STEP 1 - Question received")

        embedding_model = EmbeddingModel()

        print("STEP 2 - Embedding model loaded")

        query_embedding = embedding_model.encode(question)[0]

        print("STEP 3 - Embedding generated")

        vector_store = VectorStore()

        print("STEP 4 - Connected to ChromaDB")

        context = vector_store.search(query_embedding)

        print("STEP 5 - Search completed")

        print("Retrieved Chunks:", len(context))

        if not context:
            return "No relevant chunks found."

        prompt = f"""
You are an AI Research Assistant.

Answer ONLY using the context below.

Context:

{chr(10).join(context)}

Question:

{question}

Answer:
"""

        print("STEP 6 - Sending prompt to Groq")

        answer = GroqService.generate(prompt)

        print("STEP 7 - Groq replied")

        return answer