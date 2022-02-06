from sqlalchemy import Column, Integer, String, DateTime, Text

from db import Base

class PageSnapshot(Base):
    __tablename__ = "page_snapshots"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    url = Column(String(255), nullable=False)
    html_content = Column(Text)

    def __repr__(self):
        return "<PageSnapshot(id='%d', timestamp='%s', url='%s')>" % (self.id, self.timestamp, self.url)