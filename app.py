'''
Author: Bappy Ahmed
Email: entbappy73@gmail.com
Date: 2021-Dec-18
'''

import pickle
import streamlit as st
import numpy as np


st.header('Book Recommender System Using Machine Learning')
model = pickle.load(open('artifacts/model.pkl','rb'))
book_names = pickle.load(open('artifacts/book_names.pkl','rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl','rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl','rb'))


def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])

    for name in book_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url



def recommend_book(book_name):
    books_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=11 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                books_list.append(j)
    return books_list , poster_url       



selected_books = st.selectbox(
    "Type or select a book from the dropdown",
    book_names
)

if st.button('Show Recommendation'):
    recommended_books, poster_url = recommend_book(selected_books)

    # First row of 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_books[0])
        st.image(poster_url[0])
    with col2:
        st.text(recommended_books[1])
        st.image(poster_url[1])
    with col3:
        st.text(recommended_books[2])
        st.image(poster_url[2])
    with col4:
        st.text(recommended_books[3])
        st.image(poster_url[3])
    with col5:
        st.text(recommended_books[4])
        st.image(poster_url[4])

    # Second row of 5 columns
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(recommended_books[5])
        st.image(poster_url[5])
    with col7:
        st.text(recommended_books[6])
        st.image(poster_url[6])
    with col8:
        st.text(recommended_books[7])
        st.image(poster_url[7])
    with col9:
        st.text(recommended_books[8])
        st.image(poster_url[8])
    with col10:
        st.text(recommended_books[9])
        st.image(poster_url[9])


# To RUN
# python -m streamlit run app.py
