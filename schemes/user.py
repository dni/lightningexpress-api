from app import db, ma

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    active = db.Column(db.Boolean, default=False)
    email = db.Column(db.String, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    balance = db.Column(db.Integer)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.balance = 0
        self.active = False

    def __repr__(self):
        return '<User %r' % self.id


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'active', 'email', 'username', 'balance')

