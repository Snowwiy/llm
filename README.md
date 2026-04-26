# Proyecto 8: LLM

# Sistema Recomendador de Películas

Sistema recomendador de películas desarrollado con Python y Streamlit. El sistema analiza metadata de películas como géneros, actores, director, palabras clave y descripciones para recomendar películas similares utilizando técnicas de procesamiento de lenguaje natural (NLP) y similitud coseno.

## Descripción

Este proyecto implementa un sistema recomendador capaz de sugerir películas similares a partir de una película seleccionada por el usuario. El sistema utiliza información como:

- Géneros
- Actores
- Director
- Palabras clave
- Descripción de la película

La recomendación se realiza utilizando técnicas de vectorización de texto y cálculo de similitud entre películas.

## Tecnologías utilizadas

- Python
- Pandas
- Scikit-learn
- Streamlit
- NLP
- CountVectorizer
- Similitud coseno

## Estructura del proyecto

```text
llm/
│
├── data/
│   ├── movies_metadata.csv
│   ├── credits.csv
│   ├── keywords.csv
│   └── movies_processed.csv
│
├── src/
│   ├── app.py
│   ├── preprocess.py
│   └── recommender.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Instalación y ejecución

### 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd llm
```

### 2. Crear entorno virtual

Windows:

```bash
python -m venv .venv
```

### 3. Activar entorno virtual

PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

## Preprocesamiento de datos

Ejecutar el script de preprocesamiento:

```bash
python src/preprocess.py
```

Este proceso:

- limpia los datos
- elimina duplicados
- combina datasets
- procesa metadata
- genera la columna de similitud

Al finalizar se generará:

```text
data/movies_processed.csv
```

## Ejecución del recomendador

Ejecutar aplicación web:

```bash
streamlit run src/app.py
```

Abrir en navegador:

```text
http://localhost:8501
```

## Funcionamiento

1. Seleccionar una película desde la interfaz
2. Elegir número de recomendaciones
3. Presionar el botón "Recomendar películas"
4. El sistema mostrará películas similares junto con su nivel de similitud y resumen

## Características

- Sistema de recomendación basado en NLP
- Interfaz web interactiva
- Recomendaciones automáticas
- Procesamiento de metadata de películas
- Similitud basada en contenido

## Dataset utilizado

El proyecto utiliza datasets de películas con información de:

- metadata
- reparto
- director
- géneros
- keywords
- descripciones

## Objetivo

Desarrollar un sistema recomendador funcional aplicando técnicas de procesamiento de lenguaje natural y análisis de similitud para generar recomendaciones inteligentes de películas.

## Nota sobre datasets

Los archivos CSV originales no se incluyen en el repositorio porque superan el límite de tamaño de GitHub. Para ejecutar el proyecto, coloca los archivos `movies_metadata.csv`, `credits.csv` y `keywords.csv` dentro de la carpeta `data/`.