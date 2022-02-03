from carter_flask import db

class PageSnapshot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    html_content = db.Column(db.Text)

db.create_all()