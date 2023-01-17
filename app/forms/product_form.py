from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,IntegerField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length, URL, InputRequired, NumberRange
from app.models import User


def higher_original(form, field):
    original_price = field.data
    price = form.data['price']
    if original_price <= price:
        raise ValidationError('Original price must higher than price')


class ProductForm(FlaskForm):

    title = StringField('title', validators=[DataRequired(), Length(max=100)])
    price = FloatField('price', validators=[DataRequired(), NumberRange(min=0)])
    category_id = IntegerField('category_id', validators=[DataRequired()])
    original_price = FloatField('original_price',validators=[higher_original, NumberRange(min=0)] )
    inventory = IntegerField('inventory', validators=[NumberRange(min=0), DataRequired() ])
    desc = TextAreaField('desc', validators=[DataRequired(), Length(max=4000)])
    shipping_fee = FloatField('shipping_fee', validators=[NumberRange(min=0)])
    delivery_days = IntegerField('delivery_days', validators=[DataRequired(), NumberRange(min=0)])
    preview_image = StringField('preview_image', validators=[DataRequired(), URL()])
