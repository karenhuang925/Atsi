from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    object = [
        User(first_name="Randi",last_name="Stanmore",email="rstanmore0@twitpic.com",shop_name="Buzzdog",location="Yangliu",preview_image="https://i.etsystatic.com/iusa/c8ca0b/45545873/iusa_400x400.45545873_xx1f.jpg?version=0",password="password"),
        User(first_name="Benedikta",last_name="Cadogan",email="bcadogan1@woothemes.com",shop_name="Meeveo",location="Yasenevo",preview_image="https://i.etsystatic.com/iusa/650229/96150289/iusa_400x400.96150289_lqq4.jpg?version=0",password="password"),
        User(first_name="Bernie",last_name="Cundict",email="bcundict2@ask.com",shop_name="Feedfish",location="Calinaoan Malasin",preview_image="https://www.rd.com/wp-content/uploads/2017/09/01-shutterstock_476340928-Irina-Bg.jpg?fit=640,427",password="password"),
        User(first_name="Ealasaid",last_name="Thirwell",email="ethirwell3@biblegateway.com",shop_name="Edgeblab",location="Tambov",preview_image="https://miro.medium.com/max/1400/0*0fClPmIScV5pTLoE.jpg",password="password"),
        User(first_name="Philomena",last_name="Neumann",email="pneumann4@xrea.com",shop_name="Kaymbo",location="Caieiras",preview_image="https://i.pinimg.com/564x/31/44/7e/31447e25b7bc3429f83520350ed13c15.jpg",password="password"),
        User(first_name="Morgun",last_name="Shovelbottom",email="mshovelbottom5@acquirethisname.com",shop_name="Minyx",location="Danbury",preview_image="https://i.etsystatic.com/iusa/b98815/58739785/iusa_75x75.58739785_o1wj.jpg?version=0",password="password"),
        User(first_name="Ashely",last_name="Corkan",email="acorkan6@lulu.com",shop_name="Brainverse",location="Telaga",preview_image="https://i.etsystatic.com/iusa/0f3c8f/81063789/iusa_75x75.81063789_e6z7.jpg?version=0",password="password"),
        User(first_name="Findley",last_name="Hakewell",email="fhakewell8@networksolutions.com",shop_name="Browsecat",location="Suphan Buri",preview_image="https://i.etsystatic.com/iusa/4841fa/65993095/iusa_400x400.65993095_1xqo.jpg?version=0",password="password"),
    ]

    db.session.add_all(object)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.commit()
