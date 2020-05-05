from db import db


class ChatModel(db.Model):
    __tablename__ = 'chats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
