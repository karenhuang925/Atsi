from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Product, Category, Image

product_routes = Blueprint('products', __name__)


@product_routes.route('/')
def get_all_products():
    """
    Query for all users and returns them in a list of user dictionaries
    """
    products = Product.query.all()
    return {'Products': [product.to_dict_all_products() for product in products]}


@product_routes.route('/<int:id>')
def get_product_detail(id):
    """
    Query for a user by id and returns that user in a dictionary
    """
    product = Product.query.get(id).to_dict_detail()
    images = Image.query.filter(Image.product_id == id).all()
    def Merge(dict1, dict2):
        return(dict1.update(dict2))
    Merge(product, {'Images': [image.to_dict() for image in images]})
    print (product)
    return product
