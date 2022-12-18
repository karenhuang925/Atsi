from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func


class Image(db.Model):
    __tablename__ = 'images'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')),nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    product = db.relationship("Product", back_populates="images")

    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'product_id': self.product_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
