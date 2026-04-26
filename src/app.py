import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies_processed.csv")
    df = df.dropna(subset=["title", "soup", "overview"])
    df["soup"] = df["soup"].astype(str)
    df = df.drop_duplicates(subset=["title"]).reset_index(drop=True)

    # Limitar para que cargue rápido
    df = df.head(8000)

    return df

@st.cache_resource
def build_model(soup_data):
    vectorizer = CountVectorizer(stop_words="english", max_features=3000)
    matrix = vectorizer.fit_transform(soup_data)

    model = NearestNeighbors(metric="cosine", algorithm="brute")
    model.fit(matrix)

    return matrix, model

def recommend(movie_title, df, matrix, model, top_n):
    index = df[df["title"] == movie_title].index[0]

    distances, indices = model.kneighbors(
        matrix[index],
        n_neighbors=top_n + 1
    )

    results = []

    for distance, idx in zip(distances[0][1:], indices[0][1:]):
        results.append({
            "Película": df.iloc[idx]["title"],
            "Similitud": round(1 - distance, 3),
            "Resumen": df.iloc[idx]["overview"]
        })

    return pd.DataFrame(results)

st.set_page_config(
    page_title="Sistema Recomendador de Películas",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Sistema Recomendador de Películas")

st.write(
    "Este sistema recomienda películas similares usando metadata, reparto, género, palabras clave y similitud coseno."
)

df = load_data()

with st.spinner("Preparando modelo de recomendación..."):
    matrix, model = build_model(df["soup"].tolist())

movie_list = sorted(df["title"].dropna().unique())

selected_movie = st.selectbox(
    "Selecciona una película:",
    movie_list
)

top_n = st.slider(
    "Número de recomendaciones:",
    min_value=5,
    max_value=15,
    value=10
)

if st.button("Recomendar películas"):
    with st.spinner("Buscando recomendaciones..."):
        results = recommend(selected_movie, df, matrix, model, top_n)

    st.subheader(f"Recomendaciones basadas en: {selected_movie}")
    st.dataframe(results, width="stretch")