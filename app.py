from flask import Flask
from flask_restful import Api
from db import db
from resources.user import UserRegister
from resources.chat import Chat, ChatList
from flask_jwt import JWT
from security import authentication, identity


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'daniel'
api = Api(app)
db.init_app(app)

jwt = JWT(app, authentication, identity)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserRegister, '/register')
api.add_resource(Chat, '/chat')
api.add_resource(ChatList, '/chats')


if __name__ == '__main__':
    app.run()
