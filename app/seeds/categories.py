from app.models import db, Category, environment, SCHEMA


def seed_categories():
    object = [
        Category(name="Holiday Shop", preview_image="https://i.etsystatic.com/11046616/c/2404/1911/267/71/il/691ee4/3400104760/il_340x270.3400104760_bvbv.jpg"),
        Category(name="Jewelry & Accessories", preview_image="https://i.etsystatic.com/38800378/r/il/e09514/4399960711/il_340x270.4399960711_hp70.jpg"),
        Category(name="Clothing & Shoes", preview_image="https://i.etsystatic.com/35332829/c/2173/1727/176/195/il/dddedc/4403815693/il_340x270.4403815693_j574.jpg"),
        Category(name="Home & Living", preview_image="https://i.etsystatic.com/17032869/c/2077/1649/0/0/il/acb5a6/4285504845/il_340x270.4285504845_a13x.jpg"),
        Category(name="Wedding & Party", preview_image="https://i.etsystatic.com/5505553/c/1575/1249/0/0/il/c317d0/1521116233/il_340x270.1521116233_6p97.jpg"),
        Category(name="Toys & Entertainment", preview_image="https://i.etsystatic.com/24837011/r/il/4424a9/4290411563/il_340x270.4290411563_jphr.jpg"),
        Category(name="Art & Collectibles", preview_image="https://i.etsystatic.com/22407915/c/1827/1450/0/0/il/7886ea/4214436811/il_340x270.4214436811_qq5n.jpg"),
        Category(name="Craft Supplies", preview_image="https://i.etsystatic.com/20851371/r/il/45a57f/3336060968/il_340x270.3336060968_mi12.jpg"),
        Category(name="Gifts & Gift Cards", preview_image="https://i.etsystatic.com/8622539/r/il/5cfaa8/4270343688/il_340x270.4270343688_dgko.jpg"),
        Category(name="On Sale", preview_image="https://i.etsystatic.com/6774813/r/il/dc89b6/2215772199/il_300x300.2215772199_st90.jpg"),
    ]

    db.session.add_all(object)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the  table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_categories():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.categories RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM categories")

    db.session.commit()
