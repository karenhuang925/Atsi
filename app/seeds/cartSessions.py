from app.models import db, Csession, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_csessions():
    session = Csession(
        customer_id = 1,
    )

    db.session.add(session)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_csessions():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.csessions RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM csessions")

    db.session.commit()
