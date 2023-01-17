from flask import Blueprint, jsonify, request
from flask_login import current_user, login_required
from app.models import db, Product, Category, Image
from app.forms import ProductForm

product_routes = Blueprint('products', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

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
    form = ProductForm()
    currentuser = current_user.to_dict()
    user_id = currentuser['id']
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        newProduct = Product(
            user_id = user_id,
            preview_image = form.data['preview_image'],
            category_id = form.data['category_id'],
            title = form.data['title'],
            price = form.data['price'],
            original_price = form.data['original_price'],
            inventory = form.data['inventory'],
            sold_num = 0,
            desc = form.data['desc'],
            shipping_fee = form.data['shipping_fee'],
            delivery_days = form.data['delivery_days'],
        )
        db.session.add(newProduct)
        db.session.commit()
        
        return newProduct.to_dict_detail()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



@product_routes.route('/<int:id>', methods=["PUT"])
@login_required
def edit_product(id):

    currentuser = current_user.to_dict()
    user_id = currentuser['id']

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

    form = ProductForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        productEdit.preview_image = form.data['preview_image']
        productEdit.category_id = form.data['category_id']
        productEdit.title = form.data['title']
        productEdit.price = form.data['price']
        productEdit.original_price = form.data['original_price']
        productEdit.inventory = form.data['inventory']
        productEdit.esc = form.data['desc']
        productEdit.shipping_fee = form.data['shipping_fee']
        productEdit.delivery_days = form.data['delivery_days']
        db.session.commit()
    
        return productEdit.to_dict_detail()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 400



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
