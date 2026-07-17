from sentence_transformers import SentenceTransformer

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text):
    """
    Convert text into a semantic embedding.
    """
    return model.encode(text)