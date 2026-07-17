import pandas as pd

def get_recommendation(score):
    if score >= 85:
        return "⭐ Highly Recommended"
    elif score >= 70:
        return "✅ Recommended"
    elif score >= 50:
        return "⚠ Consider"
    else:
        return "❌ Not Recommended"


def rank_candidates(candidate_results):

    df = pd.DataFrame(candidate_results)

    df = df.sort_values(
        by="Match Score",
        ascending=False
    )

    df.reset_index(drop=True, inplace=True)

    df["Rank"] = df.index + 1

    df["Recommendation"] = df["Match Score"].apply(get_recommendation)

    return df