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

Read the research paper excerpts below.

Generate a professional report in MARKDOWN.

Use exactly these headings:

# Executive Summary

# Research Objective

# Methodology

# Key Findings

# Important Concepts

# Applications

# Conclusion

# Future Work

Requirements:

- Use markdown headings (#)
- Use bullet points
- Keep it under 500 words
- Do not include any introduction before the first heading.

Research Paper:

{context}
"""

        return GroqService.generate(prompt)