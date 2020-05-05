from flask_restful import Resource
from flask_restful import reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Must be provided')
    parser.add_argument('password', type=str, required=True, help='Must be provided')

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data['username']
        password = data['password']

        user = UserModel(username, password)
        user.save_to_db()
        return user.json()
