import os
import openai
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from flask import Flask, request
from werkzeug.utils import secure_filename

numFiles = 0
openai.api_key = open("api_key.txt").read()

app = Flask(__name__)

@app.post("/rank")
def rank_resumes():
    ranks = {}
    for key, file in request.files.items():
        global numFiles
        numFiles += 1
        ext = os.path.splitext(secure_filename(file.filename))[1]
        filePath = f"files/{numFiles}{ext}"
        file.save(filePath)
        reader = SimpleDirectoryReader(
            input_files=[filePath]
        )
        docs = reader.load_data()
        index = VectorStoreIndex.from_documents(docs)
        query_engine = index.as_query_engine()
        response = query_engine.query("Based on this resume, how would you rank their JavaScript knowledge on a scale of 1-10? Only state the number.")
        print(response)
        ranks[key] = 1 # test
    return ranks
    
