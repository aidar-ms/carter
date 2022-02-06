import requests
from bs4 import BeautifulSoup


class Parser:

    def __init__(self) -> None:
        pass

    def fetch_page(self, url: str) -> str:
        """Returns string representation of a page
        """
        resp = requests.get(url)
        bs4 = BeautifulSoup(resp.content, "html.parser")
        return str(bs4.html)
