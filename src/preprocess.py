import ast
import pandas as pd


def extract_names(text, limit=5):
    try:
        items = ast.literal_eval(text)
        return [item["name"].replace(" ", "") for item in items[:limit]]
    except:
        return []


def extract_director(text):
    try:
        items = ast.literal_eval(text)

        for item in items:
            if item.get("job") == "Director":
                return item["name"].replace(" ", "")

        return ""
    except:
        return ""


def load_data():
    movies = pd.read_csv("data/movies_metadata.csv", low_memory=False)
    credits = pd.read_csv("data/credits.csv")
    keywords = pd.read_csv("data/keywords.csv")

    movies = movies[["id", "title", "overview", "genres"]]

    movies = movies.dropna(subset=["id", "title"])
    movies = movies[movies["id"].astype(str).str.isnumeric()]
    movies["id"] = movies["id"].astype(int)

    credits["id"] = credits["id"].astype(int)
    keywords["id"] = keywords["id"].astype(int)

    df = movies.merge(credits, on="id")
    df = df.merge(keywords, on="id")

    df = df.dropna(subset=["title", "overview"])
    df = df.drop_duplicates(subset=["title"])

    return df


def prepare_data(df):
    df["genres_clean"] = df["genres"].apply(lambda x: extract_names(x))
    df["keywords_clean"] = df["keywords"].apply(lambda x: extract_names(x))
    df["cast_clean"] = df["cast"].apply(lambda x: extract_names(x, limit=3))
    df["director_clean"] = df["crew"].apply(extract_director)

    df["overview"] = df["overview"].fillna("")

    df["soup"] = (
        df["overview"] + " " +
        df["genres_clean"].apply(lambda x: " ".join(x)) + " " +
        df["keywords_clean"].apply(lambda x: " ".join(x)) + " " +
        df["cast_clean"].apply(lambda x: " ".join(x)) + " " +
        df["director_clean"]
    )

    return df


if __name__ == "__main__":
    df = load_data()
    df = prepare_data(df)

    df.to_csv("data/movies_processed.csv", index=False)

    print("Archivo procesado guardado en data/movies_processed.csv")