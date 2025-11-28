import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app


def get_db_connection():
    """Get a PostgreSQL connection using app config."""
    conn = psycopg2.connect(
        host=current_app.config.get('DB_HOST', 'localhost'),
        port=current_app.config.get('DB_PORT', '5432'),
        database=current_app.config.get('DB_NAME'),
        user=current_app.config.get('DB_USER'),
        password=current_app.config.get('DB_PASSWORD'),
    )
    return conn


def init_db():
    """Create minimal tables if they don't exist."""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            usuario VARCHAR(120) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            category VARCHARc(120),
            price NUMERIC(10,2) NOT NULL DEFAULT 0
        );
    ''')

    conn.commit()
    # If FORCE_SEED=1, clear existing rows so seed runs every startup
    if os.getenv('FORCE_SEED') == '1':
        cur.execute('TRUNCATE TABLE products, users RESTART IDENTITY CASCADE;')

    # Seed data if tables are empty
    # Seed products
    cur.execute("SELECT COUNT(*) FROM products;")
    prod_count = cur.fetchone()[0]
    if prod_count == 0:
        sample_products = [
            ("Fender Stratocaster", "Electric Guitar", 1299.99),
            ("Gibson Les Paul", "Electric Guitar", 2499.00),
            ("Boss DS-1 Distortion", "Effects Pedal", 59.99),
            ("Line 6 Spider V 60 MkII", "Amplifier", 299.99),
            ("Ernie Ball Regular Slinky", "Guitar Strings", 6.99)
        ]
        cur.executemany(
            'INSERT INTO products (name, category, price) VALUES (%s, %s, %s)',
            sample_products
        )

    # Seed users
    cur.execute("SELECT COUNT(*) FROM users;")
    user_count = cur.fetchone()[0]
    if user_count == 0:
        sample_users = [
            ("admin", "admin"),
            ("demo", "demo")
        ]
        cur.executemany(
            'INSERT INTO users (usuario, password) VALUES (%s, %s)',
            sample_users
        )

    conn.commit()
    cur.close()
    conn.close()
