from rag.embeddings import EmbeddingModel

texts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Deep Learning"
]

embeddings = EmbeddingModel.encode(texts)

print(type(embeddings))
print(embeddings.shape)