from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func


class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
    category_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('categories.id')))
    title = db.Column(db.String(400), nullable=False)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)
    inventory = db.Column(db.Integer)
    sold_num = db.Column(db.Integer)
    desc = db.Column(db.String(4000), nullable=False, unique=True)
    shipping_fee = db.Column(db.Float)
    delivery_days = db.Column(db.Datetime)
    preview_image = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    user = db.relationship("User", back_populates="products")
    category = db.relationship("Category", back_populates="products")
    cartItems = db.relationship("CartItem", back_populates="product", cascade="all, delete-orphan")
    images = db.relationship("Image", back_populates="product", cascade="all, delete-orphan")


    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'preview_image': self.preview_image,
            'title': self.title,
            'price': self.price,
            'original_price': self.original_price,
            'inventory': self.inventory,
            'sold_num': self.sold_num,
            'desc': self.desc,
            'shipping_fee': self.shipping_fee,
            'delivery_days': self.delivery_days,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


    def to_dict_all_products(self):
        return {
            'id': self.id,
            'preview_image': self.preview_image,
            'title': self.title,
            'price': self.price,
            'original_price': self.original_price,
            'sold_num': self.sold_num,
            'Vendor': {
                'id': self.user.id,
                'shop_name': self.user.shop_name,
            }
        }
