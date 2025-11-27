import click
from flask.cli import with_appcontext
from .extensions import db
from .productos.models import Product

@click.command('seed')
@with_appcontext
def seed_db():
    """Seed te databse with sample products.
    """
    products = [
        {"name": "Fender Stratocaster", "category": "Electric Guitar", "price": 1299.99},
        {"name": "Gibson Les Paul", "category": "Electric Guitar", "price": 2499.00},
        {"name": "Boss DS-1 Distortion", "category": "Effects Pedal", "price": 59.99},
    ]

    for p in products:
        product = Product(**p)
        db.session.add(product)
    
    db.session.commit()
    click.echo("Database seeded!")

def init_app(app):
    app.cli.add_command(seed_db)