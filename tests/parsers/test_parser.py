import pdb
from parsers.core import Parser


def test_hello():
    """ NOTE: Makes live HTTP requests
    """
    url = "https://engineering.atspotify.com/"
    parser = Parser()
    html = parser.fetch_page(url)

    assert type(html) is str
    assert len(html) > 0
