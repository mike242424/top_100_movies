from bs4 import BeautifulSoup
import requests

data = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')
soup = BeautifulSoup(data.text, 'html.parser')
movie_list = soup.find_all(name='h3')

movie_title = [movie.text for movie in movie_list]
reversed_movie_list = movie_title[::-1]

with open('movies.txt', 'w') as file:
    for movie in reversed_movie_list:
        file.write(movie + '\n')

