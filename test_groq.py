from services.groq_service import GroqService

answer = GroqService.generate(
    "Say hello in one sentence."
)

print(answer)