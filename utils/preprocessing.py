import re


def preprocess_text(text):
    """
    Clean extracted text before generating embeddings.
    """

    # Convert to lowercase
    text = text.lower()

    # Remove newlines
    text = text.replace("\n", " ")

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove unwanted characters
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", "", text)

    return text.strip()