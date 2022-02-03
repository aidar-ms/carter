import pdb
from parsers.core import Parser


def test_hello():
    # pdb.set_trace()
    url = "https://engineering.atspotify.com/"
    parser = Parser()
    html = parser.fetch_page(url)

    print(html)
    assert len(html) > 0

    assert type(html) is str
