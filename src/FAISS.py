# region Setup

import os
import json
import openai
import faiss
import numpy as np
from dotenv import load_dotenv

# Load key from .env
load_dotenv()

# Get OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key for embedding model
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # แทนที่ด้วย API key ของคุณ

# set function for calling embedding model
def get_embeddings(texts):
    response = client.embeddings.create(
        input=texts,
        model="text-embedding-ada-002"  # หรือโมเดลที่คุณต้องการใช้
    )
    embeddings = [record.embedding for record in response.data]
    return np.array(embeddings)

# -----------------------------------------------------------------------------------------------------------------------------------------
# region Insert

class FAISS:

    @staticmethod
    def insert(data: list, filename: str) -> None: 

        # Get embeddings
        embeddings = get_embeddings(data)

        # Create FAISS index
        dimension = embeddings.shape[1]  # ขนาดเวกเตอร์
        index = faiss.IndexFlatL2(dimension)

        # Add data into FAISS index
        index.add(embeddings)

        # Save FAISS index to file
        faiss.write_index(index, f'{filename}.index')

        # Save data to JSON file
        with open(f'{filename}.json', 'w') as f:
            json.dump(data, f)

    # -----------------------------------------------------------------------------------------------------------------------------------------
    # region Search

    @staticmethod
    def search(query: str, filename: str, k:int = 5) -> str:

        # Load saved FAISS index
        loaded_index = faiss.read_index(f'{filename}.index')

        # Load data in saved JSON
        with open(f'{filename}.json', 'r') as f:
            bugs_data = json.load(f)

        # Get query embedding
        query_embedding = get_embeddings([query])

        # Search
        distances, indices = loaded_index.search(query_embedding, k)

        # Set result
        result = ""
        for i, idx in enumerate(indices[0]):
            result += f"Matched Information: {bugs_data[idx]}\n"
            result += f"Score (Distance): {distances[0][i]:.4f}\n\n"

        return result.strip()

# -----------------------------------------------------------------------------------------------------------------------------------------
