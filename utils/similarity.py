from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(jd_embedding, resume_embedding):
    """
    Calculate similarity between Job Description and Resume.
    """

    similarity = cosine_similarity(
        [jd_embedding],
        [resume_embedding]
    )[0][0]

    return similarity * 100