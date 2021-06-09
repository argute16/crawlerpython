import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time
from .CrawledArticle import CrawledArticle


class ArticleFetcher():
    def fetch(self):
        url = "http://python.beispiel.programmierenlernen.io/index.php"
        articles = []

        while url != "":
            print(url)
            time.sleep(
                1)  # Break between the Requests. Bevor that the link will be printed. This ensures, that you will see, if you run into an infinity loopto prevent Downtime of the scraped page.
            r = requests.get(url)  #The page is opened
            doc = BeautifulSoup(r.text, "html.parser")  #the text from the page is collected

            for card in doc.select(".card"):  #The relevant Informaition is stored
                emoji = card.select_one(".emoji").text
                content = card.select_one(".card-text").text
                title = card.select(".card-title span")[1].text
                image = urljoin(url, card.select_one("img").attrs[
                    "src"])  #For prictures, where you only have a relative link, they need to be merged/joined with the page link

                yield CrawledArticle(title, emoji, content,
                                     image)  # Turns this into a generator. So that each site is only scraped at the time, when the data is necessary

            next_button = doc.select_one(".navigation .btn")
            if next_button:  #To be able to follow a button and read all pages
                next_href = next_button.attrs["href"]
                next_href = urljoin(url, next_href)
                url = next_href
            else:
                url = ""

        return articles