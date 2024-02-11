import requests
from bs4 import BeautifulSoup

# URL do site.
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Realiza a requisição.
response = requests.get(URL)

# Cria um objeto BeatufiulSoup a partir do texto retornado pela requisição.
soup = BeautifulSoup(response.text, "html.parser")

# Extrai o nome dos filmes de todas as tags <h3> com a classe "title" e os colocam em uma lista.
movies = [movie.string for movie in soup.find_all("h3", class_="title")]

# Cria o arquivo "movies.txt" e escreve o nome dos filmes no arquivo.
with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movies[::-1]:
        file.write(f"{movie}\n")