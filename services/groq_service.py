import os

from dotenv import load_dotenv
from groq import Groq, RateLimitError

load_dotenv()


class GroqService:

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    @classmethod
    def generate(cls, prompt):

        # Limit prompt size
        prompt = prompt[:10000]

        try:

            response = cls.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional AI Research Assistant."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.2,
                max_completion_tokens=350
            )

            return response.choices[0].message.content

        except RateLimitError:

            return (
                "⚠️ Groq API rate limit reached.\n\n"
                "Please wait until your quota resets or use a new API key."
            )

        except Exception as e:

            return f"Error: {str(e)}"