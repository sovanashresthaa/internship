with open("documents.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

print("Documents loaded successfully!")
print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)