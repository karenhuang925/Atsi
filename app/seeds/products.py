from app.models import db, Product, environment, SCHEMA


def seed_products():
    object = [
        Product(user_id=1,category_id=1,
                title="Check Check Wrap",
                price=10.85,
                inventory=5,
                sold_num=493,
                desc="""Roll of 3 flat sheets.
Each flat gift wrap sheet measures 20 x 30"
Printed on luxe uncoated text weight paper.""",
                shipping_fee=10,
                delivery_days=1,
                preview_image="https://i.etsystatic.com/6533187/r/il/12c7b2/3626100584/il_794xN.3626100584_r9fj.jpg"),
        Product(user_id=1,category_id=1,
                title="Blush Cupcake Birthday Card with Gold Foil",
                price=5.35,
                inventory=34,
                sold_num=440,
                desc="""Printed in the USA on beautiful warm white cotton cardstock
4 1/4" x 5 1/2"
Blank inside
Includes coordinating envelope and plastic sleeve
Ships in a durable, chip-board mailer
Gold foil accents""",
                shipping_fee=0,
                delivery_days=1,
                preview_image="https://i.etsystatic.com/6533187/r/il/358da6/2792698086/il_1140xN.2792698086_6bzt.jpg"
        ),
        Product(user_id=1,category_id=1,
                title="City Sidewalks - No. 10 Birthday Greeting Card Boxed set of 8",
                price=20.85,
                inventory=10,
                sold_num=2230,
                desc="""Printed in the USA on beautiful warm white cotton cardstock
4" x 9"
Blank inside
Includes coordinating envelope and plastic sleeve
Ships in a durable, chip-board mailer""",
                shipping_fee=0,
                delivery_days=3,
                preview_image="https://i.etsystatic.com/6533187/r/il/fbb7b7/965918152/il_794xN.965918152_793i.jpg"
        ),
        Product(user_id=2,category_id=1,
                title="Personalised Two Piece Jigsaw Decoration Set - Puzzle Piece Christmas Tree Baubles for Family Names or Couples - Seasonal Holiday Ornament",
                price=16.55,
                inventory=4,
                sold_num=39,
                desc="""This Personalised Two Piece Jigsaw Decoration Set makes a beautiful addition to your Christmas tree ornaments, perfect for families or couples.
The puzzle piece design means that the two parts can slot together, making the perfect gift for your other half or missing piece this holiday season.
Each bauble is handmade in our UK workshop from sustainably sourced oak wood, engraved with your personalisation and finished with red ribbon to hang on the Christmas tree.
When you place your order please enter the text you would like engraved on each piece, clearly labelling piece 1 and 2 (max. 40 characters per piece).
Each decoration measures approximately 45 x 45mm.""",
                shipping_fee=0,
                delivery_days=2,
                preview_image="https://i.etsystatic.com/6841042/r/il/2593d4/2531275408/il_794xN.2531275408_2yxi.jpg"
        ),
        Product(user_id=2,category_id=1,
                title="Countdown to Christmas printable, Santa's beard advent calendar, days until Christmas, kids activity, boho decor",
                price=2.02,
                original_price=2.53,
                inventory=560,
                sold_num=469,
                desc="""Countdown to Christmas, Santa's beard advent calendar.
This is an instant digital download purchase for you to print at home, take to your local print shop or upload to an online printing service.
You will receive 4 high quality JPG files including both versions of the print as shown. Included in the download are the following sizes 16"x20" and 8.5"x11". If you need another size please feel free to message me.
Find the same print with a sage background here: https://www.etsy.com/au/listing/1075691628/countdown-to-christmas-printable-santas?ref=shop_home_active_1
...............
Instant Download
After the checkout process, you will receive an email that your payment has processed and it will include a link to your download. Alternatively, to access your file, you can find them by viewing your Etsy profile and then click your purchases and reviews section.
..................
This is an instant download purchase, no product will be shipped and the frames are not included. Colours may vary slightly due to viewing different monitors. This purchase is for PERSONAL USE ONLY and the file is not to be sold or distributed in any way. Copyright remains with © Charlie & Pig 2021.""",
                shipping_fee=0,
                delivery_days=4,
                preview_image="https://i.etsystatic.com/18603489/r/il/8c02de/3395516325/il_794xN.3395516325_jq6u.jpg"
        ),
        Product(user_id=3,category_id=1,
                title="Personalized New Home Ornament - New Home Christmas Ornament - Wreath New House Ornament",
                price=14.99,
                original_price=29.98,
                inventory=20,
                sold_num=43,
                desc="""Our Award-Winning Keptsake© ceramics are 100% designed, printed, pressed and shipped (next business day!) to you from our Upstate New York boutique.
BUY WITH CONFIDENCE - We have many thousands of happy customers outside of Etsy. Help us grow our reputation here as well! All orders come with 100% SATISFACTION GUARANTEE! If for any reason you are not happy, message us for a full refund and keep the item! Otherwise, all we ask is for a review :)
This personalized 3" round ceramic ornament is hand-made and is fully customizable. Sent with ribbon (may vary from picture).
*Every item sold comes with a FREE GIFT BOX and makes the perfect gift.
📋 HOW TO ORDER:
***Every customization needs to be added individually to cart. Please do not add a quantity of more than one to your cart at a time (unless you would like them to all read the same)as only one personalization can be put in order at a time***
✧ Choose any applicable design variation from the dropdown
✧ Enter personalization details in the "add your personalization" field (follow provided directions)
✧ ADD TO CART
✧ If you are purchasing more than one ornament add them to cart one at a time with personalization
✧ Select from our shipping class options (all items shipped next day!)
✧Make sure your correct address has been updated in your Etsy account.
✧International orders may be subject to a customs fee which will need to be payed by the customer
• • • • • • • • • • • • • • • • • • • • • • • • • • • • •
📦 PRODUCTION TIME & SHIPPING
► All keepsakes are handmade-to-order, just for you!
► Production time is same or next day.
► We ship all orders next business day.
► USPS First Class, Priority and Express available at checkout
► Delivery time is 1-4 days in the US, and approx. 6-10 days internationally.
► On a deadline? Upgrade to Priority Mail Express at checkout
(1-2 day delivery US; 3-5 days international).""",
                shipping_fee=0,
                delivery_days=2,
                preview_image="https://i.etsystatic.com/20849976/r/il/ac1c3c/4483795947/il_794xN.4483795947_kkos.jpg"
        ),
        Product(user_id=4,category_id=1,
                title="Family Christmas Shirts, Christmas Matching, Dear Santa, They Did It, Family Matching Christmas Shirts, Matching Christmas Pajamas",
                price=22.85,
                inventory=10,
                sold_num=98,
                desc="""Family Christmas Shirts, Christmas Matching, Dear Santa, They Did It, Family Matching Christmas Shirts, Matching Christmas Pajamas
FREE FRONT-SIDE PERSONALIZATION.
If you want to add or change the existing part of the design feel free to write a note during the ordering process or contact me before purchase if you have any questions.
BACKSIDE PRINT - IMPORTANT!!!
Please contact me if you want to add a graphic on the backside as the overall price may increase!
SIZES:
If you are in need of 4XL or 5Xl Unisex t-shirt sizes we can do those ones too but please write before the purchase to check the availability.
MATERIALS:
- Solid colors:
100% Airlume combed, ring-spun cotton, Cotton
- Heather colors:
52% Airlume combed, ring-spun cotton, 48% poly""",
                shipping_fee=0,
                delivery_days=5,
                preview_image="https://i.etsystatic.com/17191109/r/il/8e1d21/2580903172/il_794xN.2580903172_e36k.jpg"
        ),
        Product(user_id=5,category_id=2,
                title="Recycled Copper and Turquoise Teardrop Made From Reclaimed Wood, Rose Gold Ear Wires Hypoallergenic.",
                price=28,
                inventory=100,
                sold_num=987,
                desc="""Casual geometric teardrop statement earrings made of Purpleheart, Reclaimed Mahogany, Padauk, Black Gabon Ebony, Paela, and Holly, inlaid with Kingman turquoise and Recycled Copper, finished with delicate 14k Rose gold Ear Wires. Very lightweight Eye-catching Earrings.
The longer version of this earring can be found here:
https://www.etsy.com/listing/896137956/large-recycled-copper-and-turquoise?ref=shop_home_feat_4
Wood piece measures 2.5cm long by 1.5cm wide.""",
                shipping_fee=0,
                delivery_days=5,
                preview_image="https://i.etsystatic.com/11053651/r/il/c3bc85/3023175863/il_794xN.3023175863_oshy.jpg"
        ),
        Product(user_id=5,category_id=2,
                title="Long Koa Wood Earrings with Turquoise and Recycled Copper Inlay, Stud or Dangle, Rose Gold Ear Wires",
                price=25,
                original_price=29.98,
                inventory=120,
                sold_num=98,
                desc="""These modern rectangle bar earrings are handcrafted from FSC Certified sustainable Curly Hawaiian Koa wood inlaid with crushed Arizona Turquoise and pure recycled Copper, finished with 14k rose gold findings. Hypoallergenic, lightweight, and tarnish resistant.
Also available with surgical steel Posts / Stud.
Each piece is hand cut and inlayed in Kenosha, WI.""",
                shipping_fee=3,
                delivery_days=5,
                preview_image="https://i.etsystatic.com/11053651/r/il/9d827a/3180512912/il_794xN.3180512912_jp3e.jpg"
        ),
        Product(user_id=1,category_id=2,
                title="Feather Ear Climber Sterling Silver Ear Cuff Boho Earrings Silver Earrings Modern Jewelry Gift for Her Gift for Her Christmas Gift - FES018",
                price=19.92,
                original_price=24.98,
                inventory=110,
                sold_num=9348,
                desc="""Feather Ear Climber cast in solid Sterling Silver. The earring has been carefully carved inspired by nature tree leaves. The Earring measures 7/8" (21mm) long. This design is available in three styles: Oxidized Sterling Silver, shiny Yellow Gold plated and, shiny Rose Gold plated""",
                shipping_fee=0,
                delivery_days=4,
                preview_image="https://i.etsystatic.com/10128979/r/il/4e0eb5/3887165990/il_794xN.3887165990_5jlb.jpg"
        ),
        Product(user_id=6,category_id=3,
                title="Speech Language Pathologist Gift | Speech Pathologist Sweat | Speech Shirt | Speechie Sweatshirt | SLP Hoodie | Speech Pathology",
                price=32.20,
                inventory=57,
                sold_num=98,
                desc="""Speech Language Pathologist Gift | Speech Pathologist Sweat | Speech Shirt | Speechie Sweatshirt | SLP Hoodie | Speech Pathology | Gift For Mom | SLP Sweatshirt Hoodie Shirts | SLP Gifts | Nurse Shirt | Gift For SLP
★★★Hello and welcome to my store where I try to brighten your day with a great product and create with 100% love.
★★This Sweatshirt is not oversized, you need to buy 2-3 sizes larger than you normally wear. PLEASE CHECK SIZE CHART!
★ Gildan Unisex Sweatshirt, Hoodie
50% Cotton 50% Polyester
Medium-heavy fabric (8.0 oz/yd² (271.25 g/m²))
Loose fit
Sewn in label
Runs true to size
★CARE INSTRUCTIONS
Wash inside out.
Wash in COLD water.
Do not use bleach.
Do not iron the design directly.
★IF YOU HAVE ANY CUSTOMIZATION PREFERENCES (changing the font, adding a name, changing the color etc.) PLEASE SEND US A MESSAGE.
""",
                shipping_fee=0,
                delivery_days=8,
                preview_image="https://i.etsystatic.com/31347012/r/il/95eb7c/4212686676/il_794xN.4212686676_1gp8.jpg"
        ),
        Product(user_id=7,category_id=4,
                title="Set of 13 Basket Wall Decor, Boho Wall Decor, Boho Wall Art, Wicker Round Bowl, Wicker Wall Tray, Bohemian Wall Decor, Hanger Wall Plate",
                price=79.99,
                original_price=116.98,
                inventory=160,
                sold_num=8,
                desc="""Set of 13 Basket Wall Decor, Boho Wall Decor, Boho Wall Art, Wicker Round Bowl, Wicker Wall Tray, Bohemian Wall Decor, Hanger Wall Plate, Africa Baskets, Woven Baskets Wall Decor, Christmas Gifts
The original wall set in the style of boho decor. The set consists of 13 round wicker baskets. This set is perfect for your cozy home and will decorate the walls, both in the kitchen and in the living room. You can also use this beautiful set as a gift to your beloved mother, or to your close friends for a housewarming party.""",
                shipping_fee=0,
                delivery_days=5,
                preview_image="https://i.etsystatic.com/29746526/r/il/dd53b7/4420142518/il_794xN.4420142518_fznb.jpg"
        ),
        Product(user_id=8,category_id=5,
                title="18K GOLD Huggie Hoop Earrings • Unisex Daily Wear Earrings • Minimalist Endless Hoop Earrings • WATERPROOF Jewelry • Perfect Christmas Gifts",
                price=22.30,
                original_price=37.17,
                inventory=80,
                sold_num=8,
                desc="""18K GOLD Huggie Hoop Earrings • Unisex Daily Wear Earrings • Minimalist Endless Hoop Earrings • WATERPROOF Jewelry • Perfect Christmas Gifts
This listing is for a pair of hoop earrings!""",
                shipping_fee=5,
                delivery_days=1,
                preview_image="https://i.etsystatic.com/30191108/r/il/391f20/4375900729/il_794xN.4375900729_r9nl.jpg"
        ),
        Product(user_id=8,category_id=6,
                title="Custom Wooden Handmade Music Box,Christmas Music Box,Wooden Horse Musical Carousel,Personalized Music Box,Musical Carousel,Heirloom Carousel",
                price=34.31,
                original_price=42.89,
                inventory=34,
                sold_num=56,
                desc="""Personalized Wooden Handmade Music Box,Christmas Music Box,Wooden Horse Musical Carousel,Horse Music Box, Musical Carousel,Heirloom Carousel
-NOTE-
If you place an order today, we cannot guarantee delivery before Christmas, please understand!
Very beautiful music box! Made of high-quality beech wood, entirely by hand!
There are 6 styles, birthday cake, carousel, Christmas snowflake, castle, train, ballerina.
The music and rotation method of each music box are different, please refer to the product details for specific conditions.""",
                shipping_fee=0,
                delivery_days=2,
                preview_image="https://i.etsystatic.com/38145326/r/il/7141fe/4333574324/il_794xN.4333574324_ser0.jpg"
        ),
        Product(user_id=8,category_id=7,
                title="Blazy Susan Pink 50 Count 98mm Pre Roll Cones",
                price=22.99,
                inventory=30,
                sold_num=4,
                desc="""These are the tried and true classics - the original Blazy Susan pink cones. Our pre roll cones are our most popular product line for a good reason - the #BlazyGang loves them!
Our 50 count pre roll cone jar is by far our most popular selection - a perfect size to throw in your bag when you're on the go, or to leave on your Blazy Susan rolling tray for later. Show up in style with the original pink cones by Blazy Susan. Slow and smooth is the name of the game with Blazy.""",
                shipping_fee=0,
                delivery_days=3,
                preview_image="https://i.etsystatic.com/19996044/r/il/a30dfc/4069425565/il_794xN.4069425565_offh.jpg"
        ),
        Product(user_id=8,category_id=8,
                title="Junk journal ephemera sticker mystery garb bag. Junk journal supplies, scrapbook supplies, journaling supplies, sticker pack.",
                price=4.89,
                original_price=5.99,
                inventory=1000,
                sold_num=9,
                desc="""Junk journal ephemera sticker mystery garb bag. Junk journal supplies, scrapbook supplies, journaling supplies, sticker pack.
🔴Please Read the detail🔴
You can pick in 20, 50, 75 or 100 stickers.""",
                shipping_fee=4,
                delivery_days=1,
                preview_image="https://i.etsystatic.com/19390283/r/il/3482ba/3042330688/il_794xN.3042330688_irap.jpg"
        ),
        Product(user_id=8,category_id=9,
                title="Passport Wallet in Full Grain Leather, Customized and Personalized [Tan & Dark Brown]",
                price=80,
                inventory=1,
                sold_num=99,
                desc="""Handcrafted and hand sewn, this passport wallet takes you back to an era when a quality leather wallet used to the norm rather than an exception. This wallet doesn't have vinyl/pu leather/fabric hiding the abysmal quality of the leather. There is no hiding with this one. It's out and out full grain leather, way better than genuine leather. It can hold 2 credit/debit cards and a passport.""",
                shipping_fee=0,
                delivery_days=3,
                preview_image="https://i.etsystatic.com/13775843/r/il/851d22/4316721199/il_794xN.4316721199_odon.jpg"
        ),
        Product(user_id=1,category_id=1,
                title="Custom Pet Portrait Print US | Personalised Gift | Dog Portrait | Cat Portrait | Pet Memorial",
                price=25.85,
                inventory=1,
                sold_num=38,
                desc="""Bespoke, modern art featuring your pet. Turn your pet photo into a custom pet portrait print!
Love It Guarantee - All orders come with a free preview for you to approve, including unlimited revisions to make sure you are 100% happy. In the unlikely event you don't love your preview, you can get a full refund, making your purchase completely risk free!
Print & Paw hand-illustrated custom pet portraits are the perfect way to honour the star of your home, capturing your pet's unique personality in a way where you simply cannot help but smile every time you see it.
Whether buying for yourself, as a unique gift for a fellow pet lover, or as a beautifully thoughtful pet memorial, our modern pet portraits are guaranteed to bring joy to any family home.""",
                shipping_fee=0,
                delivery_days=1,
                preview_image="https://i.etsystatic.com/25011559/r/il/8f01c7/3487753864/il_794xN.3487753864_isva.jpg"
        ),
        Product(user_id=2,category_id=1,
                title="Advent Calendar Crochet Kit. Advent Calendar For Life Giant Crochet Kit. Christmas Advent Calendar. Easy crochet pattern by Wool Couture",
                price=75.74,
                original_price=89.11,
                inventory=2,
                sold_num=98,
                desc="""Wool Couture's Christmas Advent Calendar.  How many advents have you had in your life?  This is your forever advent calendar - make one and use it forever!
Its always time for Christmas here at Wool Couture and there is no better time than now to start your new advent calendar.
""",
                shipping_fee=0,
                delivery_days=5,
                preview_image="https://i.etsystatic.com/10172021/r/il/71d8d1/2210060102/il_794xN.2210060102_pj0r.jpg"
        ),
        Product(user_id=1,category_id=1,
                title="The Americana Gift Box - 4 Jars of Handcrafted Spice Blends in Gift Box",
                price=43,
                inventory=100,
                sold_num=308,
                desc="""The Americana Gift Box - 4 Jars of Handcrafted Spice Blends in Gift Box

Some of our favorite flavors to feed the soul on hot days at the summer barbeques to the cool days when you crave comfort food, including Sweet & Smokey BBQ, Honey Mustard, Fried Chicken, and Ranch.

A beautifully packaged gift box containing 4 glass jars of our handcrafted spice blends.
""",
                shipping_fee=0,
                delivery_days=6,
                preview_image="https://i.etsystatic.com/6853759/r/il/c98466/3434563416/il_794xN.3434563416_t1rr.jpg"
        ),
        Product(user_id=3,category_id=1,
                title="Hand Embroidered, MINI/Pet/Baby SIZE, Personalized Linen Holiday Stocking, Handmade in Los Angeles",
                price=38.4,
                original_price=48.4,
                inventory=1,
                sold_num=1038,
                desc="""* This listing is for the MINI SIZE. See my shop for standard size stockings! *

ABOUT THE STOCKINGS
Why should humans get a mantle monopoly? As we all know, pets are a part of the family and while they may occasionally jump at the sound of tin foil, knock a vase off the side table, spread last night’s compost over the kitchen floor, or slobber all over your knee, I think we can all agree that they are no less deserving of a little stocking of their own.""",
                shipping_fee=0,
                delivery_days=2,
                preview_image="https://i.etsystatic.com/11046616/r/il/691ee4/3400104760/il_794xN.3400104760_bvbv.jpg"
        ),
    ]

    db.session.add_all(object)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_products():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.products RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM products")

    db.session.commit()
