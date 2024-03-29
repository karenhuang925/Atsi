from flask.cli import AppGroup
from .users import seed_users, undo_users
from .categories import seed_categories, undo_categories
from .products import seed_products, undo_products
from .images import seed_images, undo_images
from .cartSessions import seed_csessions, undo_csessions
from .cartItems import seed_citems, undo_citems


from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_citems()
        undo_csessions()
        undo_images()
        undo_products()
        undo_categories()
        undo_users()
    seed_users()
    seed_categories()
    seed_products()
    seed_images()
    seed_csessions()
    seed_citems()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_categories()
    undo_products()
    undo_images()
    undo_csessions()
    undo_citems()
