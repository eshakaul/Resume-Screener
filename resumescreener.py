import os
from llama_index import SimpleDirectoryReader, VectorStoreIndex
os.environ["OPEN_API_KEY"] = "YOUR_OPENAI_API_KEY"

reader = SimpleDirectoryReader(
    input_files=["test.txt"]
)

docs = reader.load_data()
print("Loaded " + str(len(docs)) + " documents.")

index = VectorStoreIndex.from_documents(docs)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
