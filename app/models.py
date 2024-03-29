from datetime import datetime
from config import db

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    messages = db.Column(db.JSON) 
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
