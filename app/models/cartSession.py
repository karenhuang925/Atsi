from .db import db, environment, SCHEMA, add_prefix_for_prod
from sqlalchemy.sql import func


class Csession(db.Model):
    __tablename__ = 'csessions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer,db.ForeignKey(add_prefix_for_prod('users.id')) )
    amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    user = db.relationship("User", back_populates="csessions")
    citems = db.relationship("Citem", back_populates="csession", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'amount': self.amount,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
