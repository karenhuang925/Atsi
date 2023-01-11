from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app.models import db, Product, Category, Image

product_routes = Blueprint('products', __name__)


@product_routes.route('/', methods=['GET'])
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
    return product

@product_routes.route('/', methods=['POST'])
@login_required
def create_a_product():
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    preview_image = request.json['preview_image']
    category_id = request.json['category_id']
    title = request.json['title']
    price = request.json['price']
    original_price = request.json['original_price']
    inventory = request.json['inventory']
    desc = request.json['desc']
    shipping_fee = request.json['shipping_fee']
    delivery_days = request.json['delivery_days']


    newProduct = Product(
        user_id = user_id,
        preview_image = preview_image,
        category_id = category_id,
        title = title,
        price = price,
        original_price = original_price,
        inventory = inventory,
        sold_num = 0,
        desc = desc,
        shipping_fee = shipping_fee,
        delivery_days = delivery_days,
    )


    db.session.add(newProduct)
    db.session.commit()

    return newProduct.to_dict_detail()


@product_routes.route('/<int:id>', methods=["PUT"])
@login_required
def edit_product(id):

    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    preview_image = request.json['preview_image']
    category_id = request.json['category_id']
    title = request.json['title']
    price = request.json['price']
    original_price = request.json['original_price']
    inventory = request.json['inventory']
    desc = request.json['desc']
    shipping_fee = request.json['shipping_fee']
    delivery_days = request.json['delivery_days']

    productEdit = Product.query.filter(id == Product.id).one_or_none()
    if not productEdit:
        return {
            "message": "Product couldn't be found",
            "statusCode": 404
            }, 404

    if not (productEdit.user_id == user_id):
        return {
            "message": "Forbidden",
            "statusCode": 403
            }, 403

    productEdit.preview_image = preview_image
    productEdit.category_id = category_id
    productEdit.title = title
    productEdit.price = price
    productEdit.original_price = original_price
    productEdit.inventory = inventory
    productEdit.esc = desc
    productEdit.shipping_fee = shipping_fee
    productEdit.delivery_days = delivery_days
    db.session.commit()
    return productEdit.to_dict_detail()


@product_routes.route('/<int:id>', methods=["DELETE"])
@login_required
def delete_product(id):
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    product = Product.query.filter(id == Product.id).one_or_none()
    if not product:
        return {
            "message": "product couldn't be found",
            "statusCode": 404
            }, 404

    if not (product.user_id == user_id):
        return {
            "message": "Forbidden",
            "statusCode": 403
            }, 403

    db.session.delete(product)
    db.session.commit()

    return {
        "message": "Successfully deleted",
        "statusCode": 200
    }
