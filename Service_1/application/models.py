from application import db

class Names(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(200), nullable=False, unique=False)

    def __repr__(self):
        return ''.join([
            'User: ', self.fullname
        ])