"""
Exercise: Vectorization
This script demonstrates how to get vector embeddings for text and compare their similarity.
"""
import os
import numpy as np
from openai import AzureOpenAI
from dotenv import load_dotenv
load_dotenv()

# Get config from environment variables
ENDPOINT_URL = os.getenv("ENDPOINT_URL")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
EMBEDDING_DEPLOYMENT_NAME = os.getenv("EMBEDDING_DEPLOYMENT_NAME")  # Add this for embeddings

# Initialize Azure OpenAI client
API_VERSION = os.getenv("API_VERSION", "2024-12-01-preview")
client = AzureOpenAI(
    azure_endpoint=ENDPOINT_URL,
    api_key=AZURE_OPENAI_API_KEY,
    api_version=API_VERSION
)

def get_embedding(text):
    # Use the deployment name for embeddings, not the model name
    response = client.embeddings.create(input=[text], model=EMBEDDING_DEPLOYMENT_NAME)
    return np.array(response.data[0].embedding)

def cosine_similarity(v1, v2):
    # High score (close to 1.0) means the words are 'close' in meaning
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

if __name__ == "__main__":
    # 1. Vectorize different concepts
    vec_apple = get_embedding("apple")
    vec_fruit = get_embedding("fruit")
    vec_truck = get_embedding("truck")
    # 2. Compare them
    score_close = cosine_similarity(vec_apple, vec_fruit)
    score_far = cosine_similarity(vec_apple, vec_truck)
    print(f"--- Vectorization Demo ---")
    print(f"Vector for 'apple' (first 5 dimensions): {vec_apple[:5]}...")
    print(f"Vector length: {len(vec_apple)} dimensions")
    print(f"\nSimilarity between 'apple' and 'fruit': {score_close:.4f}")
    print(f"Similarity between 'apple' and 'truck': {score_far:.4f}")
