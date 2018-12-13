from flask_login import LoginManager
class user_session(UserMixin):
    def __init__(self, email, id):
        self.email = email
        self.id = id




    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True