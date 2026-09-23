from idlelib.rpc import response_queue

import streamlit as st
import pickle
import pandas as pd
import requests
import time

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}".format(movie_id)
    params = {
        "api_key": "b7d9ce6fc191b82367e94bcc525d1ef6"
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    for _ in range(3):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            data = response.json()
            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
            break # If no poster path, break to fallback
        except requests.exceptions.ConnectionError:
            time.sleep(1)
    
    return "https://via.placeholder.com/500x750?text=No+Poster"

def recommend(movie):
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies =[]
        recommended_movies_poster = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id

            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_movies,recommended_movies_poster


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie recommender system')

selected_movie_name = st.selectbox(
    'Select a movie from the dropdown menu',
    movies['title'].values
)
if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
