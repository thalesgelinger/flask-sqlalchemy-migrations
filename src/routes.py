from app import app
from controllers.user_controller import UserController

user_ctl = UserController()

@app.route('/users')
def get_users():
    return user_ctl.index()

@app.route('/users', methods=['POST'])
def add_user():
    return user_ctl.store()

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    return user_ctl.delete(id)
