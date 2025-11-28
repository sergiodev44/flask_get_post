Flask Get/Post — Simple PostgreSQL setup

This project is a small Flask app that uses direct PostgreSQL queries (psycopg2) instead of SQLAlchemy/migrations.

## Quick start

1. Activate virtualenv:

```bash
source venv/bin/activate
```

2. Make sure PostgreSQL is running and reachable. If you need to create the DB:

```bash
sudo -u postgres createdb mi_nd_db
sudo -u postgres psql -c "CREATE ROLE myuser WITH LOGIN PASSWORD '1234';" || sudo -u postgres psql -c "ALTER ROLE myuser WITH PASSWORD '1234';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mi_nd_db TO myuser;"
```

3. Install Python deps (if not already):

```bash
pip install -r requirements.txt
# or individually:
pip install Flask python-dotenv psycopg2-binary
```

4. Start the app (development):

```bash
export FLASK_APP=unidad3_http.app:create_app
export FLASK_ENV=development
# If you want the app to truncate and reseed the DB on each startup, enable FORCE_SEED (see below)
flask run --host=127.0.0.1 --port=5000
```

## FORCE_SEED (auto reseed)

You can force the application to truncate and reseed the `products` and `users` tables every time it starts by setting `FORCE_SEED=1` in your `.env` (development only). This is handy for testing but should not be used in production.

Example `.env` snippet:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mi_nd_db
DB_USER=myuser
DB_PASSWORD=1234
SECRET_KEY=your_secret
FORCE_SEED=1
```

When `FORCE_SEED=1` the app will `TRUNCATE TABLE products, users RESTART IDENTITY CASCADE;` at startup and then insert sample data.

## Reset the DB manually

If you prefer to reset manually instead of using `FORCE_SEED`:

```bash
PGPASSWORD=1234 psql -h localhost -U myuser -d mi_nd_db -c "TRUNCATE TABLE products, users RESTART IDENTITY CASCADE;"
```

## Verify seeded data

```bash
PGPASSWORD=1234 psql -h localhost -U myuser -d mi_nd_db -c "SELECT id, name, category, price FROM products LIMIT 10;"
PGPASSWORD=1234 psql -h localhost -U myuser -d mi_nd_db -c "SELECT id, usuario FROM users LIMIT 10;"
```

## Notes
- Passwords in the demo users are stored in plaintext for simplicity (`admin/admin`, `demo/demo`). Replace with `bcrypt` hashes in production.
- The app reads `.env` automatically (we call `load_dotenv()` early in `app.py`), so you generally don't need to export DB variables manually.

If you want, I can:
- Add a small management command to reseed the DB without restarting the app
- Replace plaintext demo passwords with bcrypt and update login/registration flows

Happy to make either change — tell me which you prefer.
