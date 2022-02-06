

from parsers.core import Parser


def test_parse_spotify_blog():
    """ NOTE: Makes live HTTP requests
    """
    url = "https://engineering.atspotify.com/"
    parser = Parser()
    html = parser.fetch_page(url)

    assert type(html) is str
    assert len(html) > 0


# Code sample of saving html in PageSnapshot

# from datetime import datetime
# from db import get_session
# from models.page_snapshot import PageSnapshot

    # session = get_session()
    # ts = datetime.now()
    # ps = PageSnapshot(timestamp=ts, url=url, html_content=html)
    # session.add(ps)
    # session.commit()
