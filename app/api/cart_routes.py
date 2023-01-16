from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, User, Product, CartItem, CartSession

cart_routes = Blueprint('carts', __name__)
def Merge(dict1, dict2):
        return(dict1.update(dict2))

@cart_routes.route('/')
@login_required
def cart_info():
    currentuser = current_user.to_dict()
    user_id = currentuser['id']
    session = CartSession.query.filter(CartSession.customer_id == user_id).one().to_dict()
    items = CartItem.query.\
        filter(CartItem.session_id == session['id']).\
        filter(CartItem.quantity > 0).\
        all()

    session['amount'] = 0
    for item in items:
        total = item.product.price * item.quantity
        session['amount'] += total

    db.session.commit()

    Merge(session, {'Items': [item.to_dict() for item in items]})
    return session

@cart_routes.route('/', methods=['POST'])
@login_required
def new_cart_session():
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    existSession = CartSession.query.\
        filter(CartSession.customer_id == user_id).\
        one_or_none()
    if existSession:
        return {"errors": ["This customer's cart session already exists"]}, 403

    newSession = CartSession(
        customer_id = user_id,
        amount = 0
    )

    db.session.add(newSession)
    db.session.commit()

    return newSession.to_dict()



@cart_routes.route('/', methods=["PUT"])
@login_required
def edit_cart():
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    product_id = request.json['product_id']
    quantity = request.json['quantity']

    currentSession = CartSession.query.\
    filter(CartSession.customer_id == user_id).\
    one_or_none()

    if not currentSession:
        currentSession = CartSession(
            customer_id = user_id,
            amount = 0
        )
        db.session.add(currentSession)
        db.session.commit()

    currentSession = currentSession.to_dict()

# whether to add a cart item or just to change the quantity in cart
    theItem = CartItem.query.\
        filter(CartItem.product_id == product_id).\
        filter(CartItem.session_id == currentSession['id']).\
        one_or_none()


    if theItem:
        theItem.quantity = quantity
    else:
        newItem = CartItem(
            product_id = product_id,
            quantity = quantity,
            session_id = currentSession['id']
        )
        db.session.add(newItem)

# get all products in the session agin
    items = CartItem.query.\
        filter(CartItem.session_id == currentSession['id']).\
        filter(CartItem.quantity > 0).\
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
    currentuser = current_user.to_dict()
    user_id = currentuser['id']

    currentSession = CartSession.query.\
    filter(CartSession.customer_id == user_id).\
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
