from app.models import db, CartItem, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_cartItems():
    object = [
        CartItem(session_id = 1, product_id = 1, quantity = 3),
        CartItem(session_id = 1, product_id = 2, quantity = 1),
        CartItem(session_id = 1, product_id = 5, quantity = 2)
    ]

    db.session.add_all(object)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_cartItems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.cartItems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM cartItems")

    db.session.commit()
