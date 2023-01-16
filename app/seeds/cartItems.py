from app.models import db, Citem, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_citems():
    object = [
        Citem(csession_id = 1, product_id = 1, quantity = 3),
        Citem(csession_id = 1, product_id = 2, quantity = 1),
        Citem(csession_id = 1, product_id = 5, quantity = 2)
    ]

    db.session.add_all(object)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_citems():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.citems RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM citems")

    db.session.commit()
