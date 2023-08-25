from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Product, Citem, Csession

cart_routes = Blueprint('carts', __name__)
def Merge(dict1, dict2):
        return(dict1.update(dict2))

@cart_routes.route('/')
@login_required
def cart_info():
    """
    Query for all items in cart and return cart session total
    """
    currentuser = current_user.to_dict()
    user_id = currentuser['id']
    csession = Csession.query.filter(Csession.customer_id == user_id).one().to_dict()
    items = Citem.query.\
        filter(Citem.csession_id == csession['id']).\
        filter(Citem.quantity > 0).\
        all()

    csession['amount'] = 0
    for item in items:
        total = item.product.price * item.quantity
        csession['amount'] += total

    db.session.commit()

    Merge(csession, {'Items': [item.to_dict() for item in items]})
    return csession

@cart_routes.route('/', methods=['POST'])
@login_required
def new_cart_session():
    """
    Create new cart session if there's none for the login user
    """
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    existSession = Csession.query.\
        filter(Csession.customer_id == user_id).\
        one_or_none()
    if existSession:
        return {"errors": ["This customer's cart session already exists"]}, 403

    newSession = Csession(
        customer_id = user_id,
        amount = 0
    )

    db.session.add(newSession)
    db.session.commit()

    return newSession.to_dict()



@cart_routes.route('/', methods=["PUT"])
@login_required
def edit_cart():
    """
    Update cart items
    """
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    product_id = request.json['product_id']
    quantity = request.json['quantity']

    currentSession = Csession.query.\
    filter(Csession.customer_id == user_id).\
    one_or_none().to_dict()


# whether to add a cart item or just to change the quantity in cart
    theItem = Citem.query.\
        filter(Citem.product_id == product_id).\
        filter(Citem.csession_id == currentSession['id']).\
        one_or_none()

    if theItem:
        theItem.quantity = quantity
    else:
        newItem = Citem(
            product_id = product_id,
            quantity = quantity,
            csession_id = currentSession['id']
        )
        db.session.add(newItem)

# get all products in the session again
    items = Citem.query.\
        filter(Citem.csession_id == currentSession['id']).\
        filter(Citem.quantity > 0).\
        all()

# to calculate cart total amount
    currentSession['amount'] = 0
    for item in items:
        total = item.product.price * item.quantity
        currentSession['amount'] += total

    db.session.commit()
    Merge(currentSession, {'Items': [item.to_dict() for item in items]})
    return currentSession


@cart_routes.route('/', methods=["DELETE"])
@login_required
def delete_cart():
    """
    Delete cart if user clicked checkout
    """
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    currentSession = Csession.query.\
    filter(Csession.customer_id == user_id).\
    one_or_none()

    if not currentSession:
        return {
            "message": "Cart Session couldn't be found",
            "statusCode": 404
            }, 404

    if currentSession.customer_id != user_id:
        return {
            "message": "Forbidden",
            "statusCode": 403
            }, 403

    db.session.delete(currentSession)
    db.session.commit()

    return {
        "message": "Successfully deleted",
        "statusCode": 200
    }
