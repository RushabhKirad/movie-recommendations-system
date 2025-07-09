# 🎬 Movie Recommender System

This is a **Content-Based Movie Recommender System** built using the [MovieLens 100k dataset](https://grouplens.org/datasets/movielens/100k/). It recommends top 5 similar movies based on selected movie genres.

---

## 🔧 Features

- Content-Based Filtering using genre vectors
- Cosine Similarity for matching
- Streamlit Web UI
- Clean modular code

---

## 📁 Project Structure

movie_recommender_system/
├── data/ # Contains u.item from MovieLens
├── app/ # Streamlit app UI
│ └── app.py
├── utils/ # Core recommender logic
│ └── recommender.py
├── notebooks/ # Optional: development notebooks
│ └── movie_recommender.ipynb
├── test.py # Script to test logic before UI
├── requirements.txt
└── README.md

---

## 🚀 How to Run

1. Clone the repo or download the folder  
2. Install dependencies:

```bash
pip install -r requirements.txt
streamlit run app/app.py
```
📚 Dataset
MovieLens 100k: https://grouplens.org/datasets/movielens/100k/

Developed By
--Rushabh Kirad
