import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.content, 'html.parser')

all_h3 = soup.find_all("h2")
au = [tag.text.strip() for tag in all_h3]

au.reverse()

for name in au:
    with open("100_movies.txt", "a", encoding="utf-8") as file:
        file.write(name + "\n")
