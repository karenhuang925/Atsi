from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func


class CartItem(db.Model):
    __tablename__ = 'cartItems'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('cartSessions.id')))
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')))
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    session = db.relationship("CartSession", back_populates="cartItems")
    product = db.relationship("Product", back_populates="cartItems")

    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'product': {
                "id": self.product.id,
                "preview_image": self.product.preview_image,
                "title": self.product.title,
                "price": self.product.price,
                "original_price": self.product.original_price,
                "sold_num": self.product.sold_num,
                "delivery_days": self.product.delivery_days,
                "Vendor": {
                        "id": self.product.user.id,
                        "shop_name": self.product.user.id,
                        "preview_image": self.product.user.preview_image,
                }
            }
        }
