from rag.vector_store import VectorStore
from services.groq_service import GroqService


class SummaryService:

    @staticmethod
    def generate():

        vector_store = VectorStore()

        # Get representative chunks
        chunks = vector_store.get_top_chunks(limit=8)

        if not chunks:
            return "No uploaded document found."

        context = "\n\n".join(chunks)

        # Prevent extremely large prompts
        context = context[:12000]

        prompt = f"""
You are an expert AI Research Assistant.

Analyze the document excerpts below and create a professional report.

Keep the report concise (maximum 400 words).

Return ONLY the following sections.

## Executive Summary

## Methodology

## Key Findings

## Conclusion

## Future Work

Document:

{context}
"""

        return GroqService.generate(prompt)