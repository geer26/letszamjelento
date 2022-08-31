from app import db
from flask_login import UserMixin
import bcrypt


def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String())
    salt = db.Column(db.String())

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        salt = bcrypt.gensalt(14)
        p_bytes = password.encode()
        pw_hash = bcrypt.hashpw(p_bytes, salt)
        self.password_hash = pw_hash.decode()
        self.salt = salt.decode()
        return True

    def check_password(self, password):
        c_password = bcrypt.hashpw(password.encode(), self.salt.encode()).decode()
        if c_password == self.password_hash:
            return True
        else:
            return False

#    def get_self_json(self):
#        return {
#            'id': self.id,
#            'username': self.username,
#            'created_at': self.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
#            'is_superuser': self.is_superuser
#        }