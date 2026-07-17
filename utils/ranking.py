import pandas as pd


def get_recommendation(score):
    """
    Return recommendation label based on match score.
    """

    if score >= 80:
        return " Highly Recommended"
    elif score >= 65:
        return " Recommended"
    elif score >= 50:
        return " Consider"
    else:
        return " Not Recommended"


def rank_candidates(candidate_results):
    """
    Sort candidates by match score and generate
    ranking with recommendation labels.

    Args:
        candidate_results (list):
            List of candidate dictionaries.

    Returns:
        pandas.DataFrame:
            Ranked candidate table.
    """

    # Convert list to DataFrame
    df = pd.DataFrame(candidate_results)

    # Sort by highest match score
    df = df.sort_values(
        by="Match Score",
        ascending=False
    )

    # Reset index
    df.reset_index(
        drop=True,
        inplace=True
    )

    # Generate Rank
    df["Rank"] = df.index + 1

    # Generate Recommendation
    df["Recommendation"] = df["Match Score"].apply(
        get_recommendation
    )

    # Arrange columns in professional order
    df = df[
        [
            "Rank",
            "Candidate Name",
            "Match Score",
            "Recommendation"
        ]
    ]

    return df