from datetime import datetime

from config import base
from celery import Celery
from celery.schedules import crontab
from db import get_session
from models.page_snapshot import PageSnapshot
from parsers.core import Parser

app = Celery("celery_carter", backend=base.REDIS_URL, broker=base.REDIS_URL)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Task to parse Spotify
    sender.add_periodic_task(
        crontab(), parse_blog.s("https://engineering.atspotify.com/"), name='Parse Spotify'
    )
    # Task to parse Google
    sender.add_periodic_task(
        crontab(), parse_blog.s("https://developers.googleblog.com/"), name='Parse Google'
    )


@app.task
def parse_blog(url):
    parser = Parser()
    html = parser.fetch_page(url)

    session = get_session()
    ts = datetime.now()

    ps = PageSnapshot(timestamp=ts, url=url, html_content=html)
    session.add(ps)
    session.commit()
