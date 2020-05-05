from flask_restful import Resource, reqparse
from models.chat import ChatModel


class Chat(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Must be provided')

    def post(self):
        data = Chat.parser.parse_args()
        name = data['name']

        chat = ChatModel(name)
        chat.save_to_db()
        return chat.json()

    def get(self):
        data = Chat.parser.parse_args()
        name = data['name']

        chat = ChatModel.query.filter_by(name=name).first()
        return chat.json()


class ChatList(Resource):
    def get(self):
        return {'chats': [chat.json() for chat in ChatModel.query.all()]}