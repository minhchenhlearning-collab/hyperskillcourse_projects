import requests
from bs4 import BeautifulSoup
from http import HTTPStatus
import string
import os 


def get_specified_articles(re):
        soup = BeautifulSoup(re.text, "html.parser")
        article_lst = soup.find_all('article')
        specified_article = []
        for article in article_lst:
            if (article.find("span", attrs={"data-test": "article.type"}).text) == article_type:
                specified_article.append(article)
        return specified_article

def get_title(article):
    title = (article.find('a').text).strip()
    exclude = string.punctuation + " "
    table = str.maketrans(exclude, "_"*len(exclude))
    name = title.translate(table)
    return name


num_page = int(input())
article_type = input()
headers = {'Accept-language': 'en-US, en; q=0.5'}
url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
for i in range(1, num_page+1):
    os.makedirs(f"Page_{i}")
    response = requests.get(url, params={"page": f'{i}'}, headers=headers)
    if response:
        specified_articles = get_specified_articles(response)
        for article in specified_articles:
            link = article.find('a').attrs["href"]
            title = get_title(article)
            response = requests.get("https://www.nature.com/nature" + link, headers)
            if response:
                soup = BeautifulSoup(response.text, "html.parser")
                with open(f"Page_{num_page}/{title}.txt", "wb") as file:
                    content = (soup.find('p', attrs={'class': 'article__teaser'}).text)
                    file.write(content.encode('utf-8'))
