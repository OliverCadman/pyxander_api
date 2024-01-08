from app.database import db


class User(db.Model):
    """Model to represent a User model in DB."""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=True)
    addresses = db.relationship("Address", backref="user", lazy=True)

    def __init__(self, name, username, email, phone):
        self.name = name
        self.username = username,
        self.email = email,
        self.phone = phone