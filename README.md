# 🎬 Movie Recommender System

A content-based Movie Recommendation System built using Python, Streamlit, and Machine Learning. The system recommends 5 similar movies based on the user's selection and fetches high-quality movie posters dynamically using the TMDB API.

## ✨ Features
- **Machine Learning Powered:** Utilizes a pre-computed Cosine Similarity matrix to find relationships between movies based on their metadata (genres, overviews, etc).
- **Interactive UI:** A clean, easy-to-use web interface built entirely in Python using Streamlit.
- **Dynamic API Integration:** Automatically fetches real-time movie posters from The Movie Database (TMDB) API, with robust error-handling and connection-reset fallbacks.

## 🛠️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend/Data Processing:** Python, Pandas, Scikit-learn (Machine Learning), Pickle
- **API:** [TMDB API (The Movie Database)](https://developer.themoviedb.org/docs)

## 🚀 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dishagautamgopalani-hub/movie-recommender-system.git
   cd movie-recommender-system
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Important Note on `similarity.pkl`:**
   Because GitHub has a strict file size limit of 100MB, the `similarity.pkl` file (which contains the 184MB pre-computed similarity matrix) is **not included** in this repository. 
   *(Note for recruiters: The Machine Learning model used to generate this file was built using CountVectorizer/TF-IDF and Cosine Similarity in a separate Jupyter Notebook).*

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
