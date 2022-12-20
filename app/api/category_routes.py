from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Product, Category, Image

category_routes = Blueprint('categories', __name__)




@category_routes.route('/<name>/products')
def products(name):
    """
    Query for a user by id and returns that user in a dictionary
    """
    products = Product.query.join(Category).filter(Category.name.ilike(f'%{name}%')).all()
    print(products)
    return {'Products': [product.to_dict_category() for product in products]}
