import os
import openai
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

filesUploaded = 0
openai.api_key = open("apikey.txt").read()

app = Flask(__name__)

@app.post("/rank")
def rank_resumes():
    for file in request.files.values():
        global filesUploaded
        filesUploaded += 1
        ext = os.path.splitext(secure_filename(file.filename))[1]
        filePath = f"files/{filesUploaded}{ext}"
        file.save(filePath)
        reader = SimpleDirectoryReader(
            input_files=[filePath]
        )
        docs = reader.load_data()
        index = VectorStoreIndex.from_documents(docs)
        query_engine = index.as_query_engine()
        response = query_engine.query("What did the author do growing up?")
        print(response)
    return {
        "test": "test"
    }
    
