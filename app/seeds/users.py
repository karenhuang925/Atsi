from app.models import db, User, environment, SCHEMA


# Adds a demo user, you can add other users here if you want
def seed_users():
    object = [
        User( first_name="Randi",last_name="Stanmore",email="rstanmore0@twitpic.com",shop_name="Buzzdog",location="Yangliu",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAALrSURBVDjLbZJZSFRhGIYNRyK6iC7aLiK8qG4MifZuylxaVOymjZQKDYbEJE1nskITEpeCFAy98KIJl8LUyn0Hzd3EbVKcxlnOuMyZcUads4xzznn7Z4JJzQMv3+E/3/t87/n4fQD4rBdjqIlmNOV1zHSJYXk0n7MPZvK27lSrtSNhdKlLkbG53/vC6qoPsNovDTzVAJelF8LqL4icHhJvgGCfAj9bD2tLPBaqb2ot7YqADQBG/22nY0Y1sEZ3QXQaiHTEPAmRHYHg6CfqJWdqSGs0VgbegVIFWxfblfu8AIe6KIc31pIGE0R+hlQKkmAHJKdHkmAjsDG4lmsB0Qrz93hQn27XewHLw9mUyzZGemfIpFlILgsxLXmMHrlo8k1HAI1EFeBNg9AUnOW8gKUfz50iOwuB6YPADpP4ahJ7HMLKCDEMkB10w7XSDN78HpwpCaLDgKmc45IXYGlPNDoX+8n0CXDGF2RCFmxf78NWJ4etNhaWsghwVCYYzR2s0bngDIOYzjvxL4GlU5lt68sjcS3g9AqYiwPB6lOInoLRyklNxlzWDqxOhkGSNDB9ToS2OKLDC7D3ZMgW6+RTqxOlZIEa0B/Oesws9QiMIQasLgkL+XshMp1Y/lkJdcZRnqpKPLzhHtBtysD5ymh6dbwM9qqHfwFkstvM6p5gOuM0eu4eQuslGVqubrc0hfoqNwDcMjelnNSWP5ifKwkD1x4Oce4yRFMQ9PnnMJp8BlzdW0jqRjAVSRiMPyY0B8sSfDZfzY7y1+GFr2LXPhamoSj3PN6kn0LNtV1giRkFkYBiN5DlDzr3IppCfLX/Adx6qZAbVKVlUKkqUFRcQmL7QRquwvrHlr7f/TvSlgDF43s9La2tMJtpDA0Noz5qDxwlsQAx8ak+WCLSy31B9kBtCWgpz465cf0KExoaIgUFXZCyowJc/XFHxDmFP8zP/PA7bhvaImVCY6hv2paArdR966CSTJx1xybV6Da7z/8A2VoHSyUsj6sAAAAASUVORK5CYII=",password="GdkK7zHY"),
        User( first_name="Benedikta",last_name="Cadogan",email="bcadogan1@woothemes.com",shop_name="Meeveo",location="Yasenevo",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAHSSURBVDjLpZPbSxtREMbzL4pSpYj1VilUmmpQSCKCSLAgihFTo9Eg0TRZY5LdxJgbKYo+2AstLRbU1nfxrlmTdLPJ55nZ+OCjyYGPYQ8zv/PN7DkmAKZGZGoakN5OKSeqPfAPtk9Ca8ew+g4xvPIHQ94DWJZ/Y3DxJ94v/ID54zf0z32BbXFPpToGODZOKrPpUzxX5pmdCgPo5HrUN7kNBtjW/qKe1TORMwDW1SPeeJ0ucMzlcshms0gmkyhqVSQSCVzmdSiKAlmWEQ6HOa/TkakBxMBolUQyFRRIpQruijp/3xR0XN/ruMiXcXar4fRG4/yOsaQBoGmzpa08x0wmg1QqhVgsxoBoNMoQSZIQCATg9/s5r300YQDoV9HS9Cr+l6vspFRzQgBVOCE3j06uVJ3zX47EDIBl6RdvdG9ec6Se4/E4QqEQA4LBIO5FSz6fD16vFx6Ph/PabLIBMM9/541ypYpyzQWpqD2VKiB54YJEq2VowwC8m/tqTFU+50i9RyIR7pUK6WSKbrcbLpcLTqeT85ot6wagf3a/rnvQNCjh8S1Ib6Z3+Wb1fviMLkcWr8bTYsqbPKg2u4JWawQvhsPCdkicLEHUkCQGNPwaGwU8AG9RQVkc+5PeAAAAAElFTkSuQmCC",password="l9Q9XUy0"),
        User( first_name="Bernie",last_name="Cundict",email="bcundict2@ask.com",shop_name="Feedfish",location="Calinaoan Malasin",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIuSURBVBgZpcHNi01hAMfx73PmzHWUO0QmbiOhyQyZMYWGRhbYSfkLpKwYpSRTSikLxE7IxsrGSmJBGtSQnXfJ5CUvg+G699x5u/ec53l+zilFNtR8PkYS0xEwTQHTFJJ5dX3to6hlxQpjAn4TjbHXH5ytrgca/MmQm1i+7akNyRgFHYv6LjYbY0BkBMZg69+Xfn109INA/NJUaJFcOjr+efAgcDkkZ1XHJzMaX87hkiYIWjCmSFTaTGndiQIS4EEeECaYtWD4at8R4HJILjWBfIJLCsgLP/WedOIr46N3aI4WglLwCZIFLMWOQwXkF5MJyRlF3k6RTIKSCdKxGsWOnUTzOgEDCPAgAcKEc8AFIZmQXBoQzmxlTuduwIOE8PjkE7Z6C7kY2RjZGnLjRG2HoSFyIblUkqvjJ58gFyM3hmwVn1aQi8FWGRyucPedI56aIrX76Qlc2A6E5BpI3uLTb8jGyMXIVpGNkatw42WFp/UimzauoW1uO7efX+Hes5HwUn/pVEAukQwO2R/IllH6HdkysmVkK1x7UWV1RzcucHQv3IozKb2rNpDZG5BR4it2shyn4wVvJ4vYxnxc0oZ3y/BuJaO1Ms1mFts795E7sPkCy1q7yEQhGdUbJ9+c37EOsQVDkb/UapXo+ch9Ho8MMbD1Isdv7iJqmkGmbiTxL739pWNtS2Yf3tDVR/uCHoa/POT+kyE+vo1PG0n8j97+0nFgD1AExoCzD86MDPwE/3Mt+7fw600AAAAASUVORK5CYII=",password="o43A4EbZV"),
        User( first_name="Ealasaid",last_name="Thirwell",email="ethirwell3@biblegateway.com",shop_name="Edgeblab",location="Tambov",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAH8SURBVDjLjZPLaxNRFIfHLrpx10WbghXxH7DQx6p14cadiCs31Y2LLizYhdBFWyhYaFUaUxLUQFCxL61E+0gofWGLRUqGqoWp2JpGG8g4ybTJJJm86897Ls4QJIm98DED9/6+mXNmjiAIwhlGE6P1P5xjVAEQiqHVlMlkYvl8/rhQKKAUbB92u91WSkKrlcLJZBK6rptomoZoNApFUbhElmU4HA4u8YzU1PsmWryroxYrF9CBdDqNbDbLr0QikUAsFkM4HOaCVCoFesjzpwMuaeXuthYcw4rtvG4KKGxAAgrE43FEIhGzlJQWxE/RirQ6i8/T7XjXV2szBawM8yDdU91GKaqqInQgwf9xCNmoB7LYgZn+Oud0T121KfiXYokqf8X+5jAyR3NQvtzEq96z4os7lhqzieW6TxJN3UVg8yEPqzu38P7xRVy+cPoay52qKDhUf0HaWsC3xRvstd3Qvt9mTWtEOPAJf/+L8oKAfwfLnil43z7Bkusqdr2X4Btvg1+c5fsVBZJ/H9aXbix/2EAouAVx4zVmHl2BtOrkPako2DsIwulexKhnG/cmfbg+uIbukXkooR/I5XKcioLu+8/QNTyGzqE36OidQNeDJayLe7yZBuUEv8t9iRIcU6Z4FprZ36fTxknC7GyCBrBY0ECSE4yzAY1+gyH4Ay9cw2Ifwv9mAAAAAElFTkSuQmCC",password="atkaQIRhNg"),
        User( first_name="Philomena",last_name="Neumann",email="pneumann4@xrea.com",shop_name="Kaymbo",location="Caieiras",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAQAAAC1+jfqAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAABjSURBVCjPY/zPgB8wMVCqgAVElP//x/AHDH+D4S8w/sWwl5GBgfE/MSZAQNL/31CdMHiGaBNS/yPbjIC3SHSD+3+EXoh5z4k2wfs/qt2/ofAziW7Q+v8brhsSrn+IMYFgZAEAE0hMH/VkcbsAAAAASUVORK5CYII=",password="WCixQMba0"),
        User( first_name="Morgun",last_name="Shovelbottom",email="mshovelbottom5@acquirethisname.com",shop_name="Minyx",location="Danbury",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAIzSURBVDjLpZNPSFRRFMa/NzPaPNSpsDQVF4JUi3YtomW0MBCchbSxhS3chAS6mJpFBYmugpjSRS5cWAQFSUmBGIYiCbYYbOyfOAqKgwgqRNF79953zzktxoEspyAvnM095/zOdy/fcUQE+zmhYomOl23J9mcXw/8N0J5u8z09+C+AU3hC58Tl+kDbVqODpkCb09UVNUeNMciuLt0b757q+ivgyuv2s4EOrteW1cZj0YOIlrpw4ECRxvsvGWSXlvpme9M39gKEN84s1xtt+o5XnojXHapDAAsWxpa3BUcc5NZz2NzYfLf+NV567lQs+8cfKN+0HnNr4pVlR6CshlYai6tZGN8inZnD4kJ2YO7ux2sAUjef5NzfARHlqabyynIoq/DN+47x6fE1rYKRQJvzRgfpD/cXrgIAszSySAJAz24Fnr7wNjOD529eYGxyDL6nR2Z7093KN0+1CjoKhcwMIk4mhlcadkkQkaLxYNJvGJjwRkUEiYcr0v8qJ11Dy6O/1uzpg6Fp5Q5OqVuW5JMlaQEAIoYbBg6XhVs6BxebixppaFo1W8Z8VYVz+2R1xLWU94klxg9FiIYBaznV0f/ZBYBIoXF4RjdYklTMdVoqDjgoCQOBFRDn89YyfMMgZlTFShrXtv0EgJ7I41njWpKEJUlWx0JueakDQwITACQAcV4BEUGZEAqKiDh56U7mUcSSzFuSRsvA6jbBksBSfjKxYKcflhgr2wpMvHMvLrOknP2u80/X2WfmmbX8IwAAAABJRU5ErkJggg==",password="uqNv8TG84l8"),
        User( first_name="Ashely",last_name="Corkan",email="acorkan6@lulu.com",shop_name="Brainverse",location="Telaga",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAJVSURBVDjLlZPbS5NhHMd3tbvyov6HIJRuhKAFgRci5GXYVQkG0c6HJGvD1FVMjdxC22wlQ9iG7uBh0rtDmxtb77vFoh2c7KgMtiGbU9xdgezb3hf0Ii3cxZfngef5fn6H5/ewALD+Vv8Upeh7HfzdM+pb4QwT7PPunOg8M7tlPh63JtE/4UM3f7WnLUDL3NE7vgmFKYbeF050Di3dbQvQSrvjzogTIm0Yt0WrePp25VNbAHcgrLopXMOgyo/uR8v4bAnAbrdLLwSIRCLK1HYaHKEdnQ9MuHZ/Edv5MpYcHljc1K9Fgvo+uxqanLYEr5wBhMNhZTqdRr1ex6jOBz8VxzONC+VyGQcHB5g3rcFGZWH+lscrc9ArWdjseqzzXWLMFEWdmnO5HEwbEYzpvmKZ+IFKpYJSqQS/3w/l+4XmlCXYnHGmMfTBOzyg9lxmkSQ5RpsbjQYKhQKy2Syz7u/vM0Z6T5+73W44nU7IlOrmS9tPPJn3VfsmXVdZLfKbra0tVKtV7O7uYmdnh8mEBtCwVCqFRCIBgiCg0Wggk8ko7sdNCMwJ3JogRpgSHA6HOhqN4ujoCIeHh6jVashkMkgmk4jH4wgEApibm4NUKqVEIhH74awXrfSPbyi+dJ020Wg0vguFQtjb20M+n2eixmIxBqDX6+nIpFAoZMb63owHHCXhOvOMWq1W7fF4UCwWQZdFN9RqtdKRSYFAcPonrj/fGPznIKlUKvX6+jrTfZvNBolEQvL5fPaFJ5GWXC5XGwwGiMViksfjtfcbT9Rq1gCXy/2vmdYfaGviUGKvapgAAAAASUVORK5CYII=",password="LO1x4NYv4"),
        User( first_name="Regen",last_name="Cowdroy",email="rcowdroy7@sitemeter.com",shop_name="Demimbu",location="Penápolis",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAInSURBVDjLhZPda9NQHIbzVwlWryzthpWuIpWOieKYZXO2q1vC0KFr9aZM3Yr40QunspU2TVYmYhVRvNErwQtR3E0JTq3G2o80mc0Ql9dzTr/SYdnFA8k5yft78nLCjcxJNwKzsuoOiZoj2GKsi3NS1I7y4hIA7n9wgQvyz4KiWLphwNgyoRMq+jZ+MUyo1ToOR6Ra3wA6ua4b8F/2gL830WF8YRGB2VX4hBwOBEWrnxl3kGzQyXzyLJbfLuL+uwQevr+Jk7EsiBn2MmMBdbJ58UEEKx9vYfVDE89MBtTsTVjA53iiy/XbeD4XRaluwhWSNRZQIYmeay6cSsYxfCmFwfMpEGW4wjk4gxm4J7IECd6IhOW7z/AlkYRaawXQbyuTtCOJAQzPp/bU9gtrLOBHrUECJI3bP5bWypoJx7l9cE+tMO0TsTuIpl90uCq+xJnoEtP2hUV8Cp7G90orwMECGthQd5gynRxLPUWuoOOR8huPN//gyde/iMuvmLZvKgtlfBTFdsBgSNwslavQiOIACaCF0ofzRQv5bzsd6BrV9obSyI8EUCw34JwkAcd4aWFoWn5N00ihFi30+HwaM5LCmM4UGH5SLtX28uvMtlg2mwH2U9UuNHBlDUKu2ANdo9pDwjqqpNQSOwdyrSegXeih0Rh7wQ5da2lbdDI5RBqxT/Qa2ArdUK1ddLV7/gX7jb1QzdhGjVAl10262n0D7IXSSbtpa9vf+QeB6/JTIb6VuwAAAABJRU5ErkJggg==",password="JuLV4C9MGRTc"),
        User( first_name="Findley",last_name="Hakewell",email="fhakewell8@networksolutions.com",shop_name="Browsecat",location="Suphan Buri",preview_image="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAAAJdSURBVDjLpZP7S1NhGMf9W7YfogSJboSEUVCY8zJ31trcps6zTI9bLGJpjp1hmkGNxVz4Q6ildtXKXzJNbJRaRmrXoeWx8tJOTWptnrNryre5YCYuI3rh+8vL+/m8PA/PkwIg5X+y5mJWrxfOUBXm91QZM6UluUmthntHqplxUml2lciF6wrmdHriI0Wx3xw2hAediLwZRWRkCPzdDswaSvGqkGCfq8VEUsEyPF1O8Qu3O7A09RbRvjuIttsRbT6HHzebsDjcB4/JgFFlNv9MnkmsEszodIIY7Oaut2OJcSF68Qx8dgv8tmqEL1gQaaARtp5A+N4NzB0lMXxon/uxbI8gIYjB9HytGYuusfiPIQcN71kjgnW6VeFOkgh3XcHLvAwMSDPohOADdYQJdF1FtLMZPmslvhZJk2ahkgRvq4HHUoWHRDqTEDDl2mDkfheiDgt8pw340/EocuClCuFvboQzb0cwIZgki4KhzlaE6w0InipbVzBfqoK/qRH94i0rgokSFeO11iBkp8EdV8cfJo0yD75aE2ZNRvSJ0lZKcBXLaUYmQrCzDT6tDN5SyRqYlWeDLZAg0H4JQ+Jt6M3atNLE10VSwQsN4Z6r0CBwqzXesHmV+BeoyAUri8EyMfi2FowXS5dhd7doo2DVII0V5BAjigP89GEVAtda8b2ehodU4rNaAW+dGfzlFkyo89GTlcrHYCLpKD+V7yeeHNzLjkp24Uu1Ed6G8/F8qjqGRzlbl2H2dzjpMg1KdwsHxOlmJ7GTeZC/nesXbeZ6c9OYnuxUc3fmBuFft/Ff8xMd0s65SXIb/gAAAABJRU5ErkJggg==",password="XHxtiTVtGYo"),
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
