from bs4 import BeautifulSoup
# import lxml
with open("./33.website.html", encoding="utf8") as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')
# print(soup.title.string)
# print(soup.prettify())
# print(soup.find_all(name="li"))
print(soup.find(id="name"))




