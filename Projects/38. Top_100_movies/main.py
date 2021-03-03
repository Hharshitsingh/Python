import requests
from bs4 import BeautifulSoup
URL = "https://www.rottentomatoes.com/top/bestofrt/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
data = soup.find(name="table", class_ = "table")
# print(data)
all_movies = data.find_all(name = "a", class_ = "unstyled articleLink")
# print(all_movies)
movies = []
# print(all_movies)
for movie in all_movies:
    movi = movie.get_text()
    movi = movi[12:]
    movies.append(movi.replace("\n",""))
    # print(movi.replace("\n",""))
print(movies)

i = 0
with open("movies.txt", mode="w") as file:
    for movie in movies:
        i+=1
        file.write(f"{i}. {movie}\n")