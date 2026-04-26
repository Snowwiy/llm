import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_processed_data():
    df = pd.read_csv("data/movies_processed.csv")

    df["soup"] = df["soup"].fillna("")

    return df


def build_similarity(df):
    vectorizer = CountVectorizer(
        stop_words="english",
        max_features=5000
    )

    matrix = vectorizer.fit_transform(df["soup"])

    similarity = cosine_similarity(matrix)

    return similarity


def recommend(movie_title, df, similarity, top_n=10):
    titles = df["title"].str.lower().reset_index(drop=True)

    movie_title = movie_title.lower()

    if movie_title not in titles.values:
        return None

    index = titles[titles == movie_title].index[0]

    distances = list(enumerate(similarity[index]))

    distances = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    recommendations = []

    for i, score in distances[1:top_n + 1]:
        recommendations.append({
            "Película": df.iloc[i]["title"],
            "Similitud": round(score, 3),
            "Resumen": df.iloc[i]["overview"]
        })

    return pd.DataFrame(recommendations)


if __name__ == "__main__":
    df = load_processed_data()

    similarity = build_similarity(df)

    results = recommend(
        "Toy Story",
        df,
        similarity,
        top_n=10
    )

    print(results)