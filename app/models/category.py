from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func


class Category(db.Model):
    __tablename__ = 'categories'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    preview_image = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    products = db.relationship("Product", back_populates="category", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'preview_image': self.preview_image,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
