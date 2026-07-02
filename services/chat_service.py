from rag.embeddings import EmbeddingModel
from rag.vector_store import VectorStore
from services.groq_service import GroqService


class ChatService:

    @staticmethod
    def ask(question):

        embedding_model = EmbeddingModel()

        query_embedding = embedding_model.encode(question)[0]

        vector_store = VectorStore()

        context = vector_store.search(query_embedding)

        print("=" * 60)
        print("QUESTION:")
        print(question)
        print("=" * 60)

        print("RETRIEVED CONTEXT:")
        print(context)
        print("=" * 60)

        if not context:
            return "No relevant chunks found in ChromaDB."

        prompt = f"""
You are an AI Research Assistant.

Answer ONLY from the provided context.

If the answer is not present, reply exactly:

I couldn't find that information in the uploaded document.

Context:

{chr(10).join(context)}

Question:
{question}

Answer:
"""

        print("PROMPT LENGTH:", len(prompt))

        answer = GroqService.generate(prompt)

        print("=" * 60)
        print("AI ANSWER:")
        print(answer)
        print("=" * 60)

        return answer