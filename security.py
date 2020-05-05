from models.user import UserModel


def authentication(username, password):
    user = UserModel.query.filter_by(username=username).first()
    if user and user.password == password:
        return user
    return None


def identity(payload):
    user_id = payload['identity']
    return UserModel.query.filter_by(id=user_id).first()
