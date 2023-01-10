from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(265), nullable=False)
    preview_image = db.Column(db.String(2550))
    shop_name = db.Column(db.String(40))
    location = db.Column(db.String(40))

    products = db.relationship('Product', back_populates='user', cascade="all, delete-orphan")
    cartSessions = db.relationship('CartSession', back_populates='user', cascade="all, delete-orphan")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'preview_image': self.preview_image,
            'email': self.email
        }

    def to_profile_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'preview_image': self.preview_image,
            'email': self.email,
            'shop_name': self.shop_name,
            'location':self.location
        }


    def to_dict_vendor_info(self):
        return {
            'id': self.id,
            'shop_name': self.shop_name,
        }
