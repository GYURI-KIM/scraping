import requests
from bs4 import BeautifulSoup
import csv

movie_data = []


url = 'https://movie.naver.com/movie/running/current.nhn#'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

movie_section = soup.select(
    "#content > .article > .obj_section > .lst_wrap > ul > li" )   # #wrap > #container써도 됨

for movie in movie_section:
    a_tag = movie.select_one('dl > dt > a')

        
    movie_name = a_tag.text
    movie_link = a_tag['href'].split("=")[1]

    movie_data = {
        'name': movie_name,
        'link': movie_link}


    with open('./0804_movie.csv', 'a', encoding="utf-8") as csvfile:
        fieldnames = ['name', 'link']
        csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
        csvwriter.writerow(movie_data)

for data in movie_data:
    print(data)