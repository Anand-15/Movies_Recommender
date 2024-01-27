import streamlit as st
import pickle
import pandas as pd
import requests
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4OTFlNDhhMDZhYjE1NTViZjY0YzdiN2Q4NGFmMzYwOSIsInN1YiI6IjY1YjNlZmQ2YjMzMTZiMDEzMGEwYmIxYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BOJ918jOk8lOyPWIhRtE4HDl3zEPeVXY2Ku_t9bQFyY"
}

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers)
    data=response.json()
    return "http://image.tmdb.org/t/p/w500/"+data["poster_path"]

def recommend(movie):
    movies_lst = []
    movies_poster=[]
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    lst_of_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for index in lst_of_movies:
        movie_id=movies.iloc[index[0]].movie_id
        movies_lst.append(movies["title"][index[0]])
        #fetch poster path from API
        movies_poster.append(fetch_poster(movie_id))
    return movies_lst,movies_poster
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movies Recommender System')
selected_movie_name = st.selectbox(
    'Select a movie which you like : ',
    movies["title"].values)
if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5,gap="medium")

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


