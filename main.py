import time
import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.title("Movies Recommender System")

movies_list = pd.read_pickle('movies.pkl')  # Load movies as a DataFrame
similarity_file = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies_list['title'].tolist()

def recommendor(movie):
    if movie in movies_list:
        movie_index = movies_list.index(movie)
        distance = similarity_file[movie_index]
        recommended_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies_list = []
        for j in recommended_movies:
            recommended_movies_list.append(movies_list[j[0]])

        return recommended_movies_list
    else:
        return []

selected_movie = st.selectbox('Select your movie', movies_list)

button = st.button('Recommend')
if button:
    recommendations = recommendor(selected_movie)
    for i in recommendations:
        st.write(i)

    success_message = st.empty()
    success_message.success('Recommended')
    time.sleep(2)
    success_message.empty()
