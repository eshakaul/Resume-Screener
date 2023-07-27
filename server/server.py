import os
import openai
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from flask import Flask, request
from werkzeug.utils import secure_filename

numFiles = 0
openai.api_key = "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"

app = Flask(__name__)

@app.post("/feedback")
def get_feedback():
    global numFiles
    numFiles += 1
    file = list(request.files.values())[0]
    ext = os.path.splitext(secure_filename(file.filename))[1]
    filePath = f"files/{numFiles}{ext}"
    file.save(filePath)
    reader = SimpleDirectoryReader(
        input_files=[filePath]
    )
    docs = reader.load_data()
    index = VectorStoreIndex.from_documents(docs)
    query_engine = index.as_query_engine()
    response = query_engine.query("Please state five pros and three cons of this resume.")
    print(str(response))
    return str(response)

# open -a Google\ Chrome --args --disable-web-security --user-data-dir="/Users/Esha/Library/ApplicationSupport/Google/Chrome"
