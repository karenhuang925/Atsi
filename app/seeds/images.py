from app.models import db, Image, environment, SCHEMA


def seed_images():
    object = [
        Image(product_id=1,url="https://i.etsystatic.com/iap/4bbbae/4474923225/iap_640x640.4474923225_7vqkswdr.jpg?version=0"),
        Image(product_id=4,url="https://i.etsystatic.com/6841042/r/il/8e42c2/4477203173/il_794xN.4477203173_1i7u.jpg") ,
        Image(product_id=4,url="https://i.etsystatic.com/6841042/r/il/1df875/2531275530/il_794xN.2531275530_ioja.jpg") ,
        Image(product_id=5,url="https://i.etsystatic.com/18603489/r/il/b27c9c/3347816154/il_794xN.3347816154_g8la.jpg") ,
        Image(product_id=5,url="https://i.etsystatic.com/18603489/r/il/bce5a3/3347816236/il_794xN.3347816236_gl57.jpg") ,
        Image(product_id=5,url="https://i.etsystatic.com/18603489/r/il/3d9c11/3347816288/il_794xN.3347816288_l25g.jpg") ,
        Image(product_id=6,url="https://i.etsystatic.com/20849976/r/il/681707/4106927632/il_794xN.4106927632_m1su.jpg") ,
        Image(product_id=6,url="https://i.etsystatic.com/20849976/r/il/c34880/3458093900/il_794xN.3458093900_iz3t.jpg") ,
        Image(product_id=6,url="https://i.etsystatic.com/20849976/r/il/557c67/3508257751/il_794xN.3508257751_i5tx.jpg") ,
        Image(product_id=6,url="https://i.etsystatic.com/20849976/r/il/46ef4c/3524905941/il_794xN.3524905941_hxmq.jpg") ,
        Image(product_id=6,url="https://i.etsystatic.com/20849976/r/il/d4393c/3505759551/il_1140xN.3505759551_8vgm.jpg") ,
        Image(product_id=7,url="https://i.etsystatic.com/17191109/r/il/d3b000/3363796751/il_794xN.3363796751_q2mw.jpg") ,
        Image(product_id=7,url="https://i.etsystatic.com/17191109/r/il/919b42/3363793201/il_794xN.3363793201_ndic.jpg") ,
        Image(product_id=7,url="https://i.etsystatic.com/17191109/r/il/69873f/3316100052/il_794xN.3316100052_5ag0.jpg") ,
        Image(product_id=7,url="https://i.etsystatic.com/17191109/r/il/78a20c/3316100188/il_794xN.3316100188_d1lp.jpg") ,
        Image(product_id=7,url="https://i.etsystatic.com/17191109/r/il/32136b/3363793587/il_794xN.3363793587_ikka.jpg") ,
        Image(product_id=8,url="https://i.etsystatic.com/11053651/r/il/92e2c5/2834304487/il_794xN.2834304487_duaz.jpg") ,
        Image(product_id=8,url="https://i.etsystatic.com/11053651/r/il/ff5e4b/2669541566/il_794xN.2669541566_81v1.jpg") ,
        Image(product_id=10,url="https://i.etsystatic.com/10128979/r/il/f180da/3443716782/il_794xN.3443716782_rjnj.jpg") ,
        Image(product_id=10,url="https://i.etsystatic.com/10128979/r/il/22beb6/3443715680/il_794xN.3443715680_jurd.jpg") ,
        Image(product_id=10,url="https://i.etsystatic.com/10128979/r/il/c9a1aa/3934659115/il_794xN.3934659115_r2my.jpg") ,
        Image(product_id=10,url="https://i.etsystatic.com/10128979/r/il/fdd26f/3491384535/il_794xN.3491384535_c7eo.jpg") ,
        Image(product_id=11,url="https://i.etsystatic.com/31347012/r/il/9ba1a8/4260340583/il_794xN.4260340583_mky4.jpg") ,
        Image(product_id=11,url="https://i.etsystatic.com/31347012/r/il/336ba8/4260340711/il_794xN.4260340711_3lyu.jpg") ,
        Image(product_id=11,url="https://i.etsystatic.com/31347012/r/il/0ceaf8/4212685528/il_794xN.4212685528_py5a.jpg") ,
        Image(product_id=12,url="https://i.etsystatic.com/29746526/r/il/63eb8e/4467521699/il_794xN.4467521699_kaiz.jpg") ,
        Image(product_id=12,url="https://i.etsystatic.com/29746526/r/il/3bd145/4467508957/il_794xN.4467508957_5j43.jpg") ,
        Image(product_id=12,url="https://i.etsystatic.com/29746526/r/il/f6a1c1/4467517949/il_794xN.4467517949_3a4p.jpg") ,
        Image(product_id=13,url="https://i.etsystatic.com/30191108/r/il/a50bce/4328500214/il_794xN.4328500214_obsp.jpg"),
        Image(product_id=13,url="https://i.etsystatic.com/30191108/r/il/1ba938/4375896757/il_794xN.4375896757_dsi5.jpg"),
        Image(product_id=14,url="https://i.etsystatic.com/38145326/r/il/43d06c/4380917599/il_794xN.4380917599_oqhq.jpg"),
        Image(product_id=14,url="https://i.etsystatic.com/38145326/r/il/65065e/4380895679/il_794xN.4380895679_fw6g.jpg"),
        Image(product_id=14,url="https://i.etsystatic.com/38145326/r/il/7c4561/4333500716/il_794xN.4333500716_sde1.jpg"),
        Image(product_id=14,url="https://i.etsystatic.com/38145326/r/il/d15ba5/4380895979/il_794xN.4380895979_ic22.jpg"),
        Image(product_id=15,url="https://i.etsystatic.com/19996044/r/il/3bfccc/3296964983/il_794xN.3296964983_j3fo.jpg"),
        Image(product_id=16,url="https://i.etsystatic.com/19390283/r/il/2d7d7b/2651755720/il_794xN.2651755720_f2pd.jpg"),
        Image(product_id=16,url="https://i.etsystatic.com/19390283/r/il/addec7/2651768724/il_794xN.2651768724_e0pe.jpg"),
        Image(product_id=18,url="https://i.etsystatic.com/25011559/r/il/788bb1/3487749732/il_794xN.3487749732_o631.jpg"),
    ]

    db.session.add_all(object)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the  table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_images():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.images RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM Images")

    db.session.commit()
