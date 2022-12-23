from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Product, Category, Image

category_routes = Blueprint('categories', __name__)




@category_routes.route('/<name>/products')
def products(name):
    products = Product.query.join(Category).filter(Category.name.ilike(f'%{name}%')).all()
    return {'Products': [product.to_dict_category() for product in products]}

@category_routes.route('/')
def categories():
    categories = Category.query.all()
    return {'Category': [category.to_dict() for category in categories]}
