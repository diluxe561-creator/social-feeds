from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(300))
    likes = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)
