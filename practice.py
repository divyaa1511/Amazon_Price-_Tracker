from bs4 import BeautifulSoup
import lxml


import os
path = os.getcwd()
html=os.path.join(path,"index.html")
# print(html)

with open(html,'r') as file:
    body = file.read()

soup = BeautifulSoup(body,'lxml')
# print(soup)
# print("------------------------")
# print(soup.prettify())

first_movie = soup.select('.movie')
all_movies = soup.find_all('div',class_="movie")
# for movie in first_movie:
    # print('-------')
    # print(movie.getText())

movie_box = soup.select_one("#movie-box")
# print(movie_box)
parent = movie_box.parent
# print(parent)
children = movie_box.children
for child in children:

    print(child)