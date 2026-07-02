import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection("papers")

print("=" * 60)
print("Collection Count:", collection.count())
print("=" * 60)

results = collection.get()

print("Number of Documents:", len(results["documents"]))

print("=" * 60)

print("First Metadata:")

print(results["metadatas"][0])

print("=" * 60)

print("First Chunk:")

print(results["documents"][0][:500])

print("=" * 60)