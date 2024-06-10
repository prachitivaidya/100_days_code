from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

# print(soup.prettify())

all_movies = soup.find_all("h3", class_= "title")
# print(all_movies)

movie_titles = [movie.get_text() for movie in all_movies]
movies = movie_titles[::-1]  # reverse the list start stop and step for n in range(len(movie_titles) -1, -1,-1)

with open("movies.txt", "w") as movies_file:
    for movie in movies:
        movies_file.write(f"{movie}\n")

# response = requests.get("https://news.ycombinator.com/news")
#
# yc_web_page = response.text
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="a")
#
# print(article_tag)
#


# with open ("website.html") as file:
#     contents = file.read();
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.p)
#
# all_p = soup.findAll("a")
# # print(all_p)
# for tag in all_p:
#     # print(tag.get_text())
#     # print(tag.get("href"))
#     pass
# heading = soup.find(name="h1", id = "name")
# print(heading.get_text())
#
# section_heading = soup.find(name="h3", class_ = "heading")
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector=" p a")
# print(company_url.get("href"))
#
# headings = soup.select(".heading")
# print(heading)