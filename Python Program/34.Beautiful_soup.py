from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.find_all("a", class_="storylink"))
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_ = "score")]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
# print(largest_index)
print("Most Popular article")
print(article_texts[largest_index])
print(article_links[largest_index])
print(largest_number)
# print(article_upvotes)