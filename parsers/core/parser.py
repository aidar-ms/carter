import requests
from bs4 import BeautifulSoup


class Parser:

    def __init__(self) -> None:
        pass

    def fetch_page(self, url: str):
        """Returns string representation of a page
        """
        resp = requests.get(url)
        bs4 = BeautifulSoup(resp.content, "html.parser")

        return bs4.contents
