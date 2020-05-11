# flask-crud

A simple CRUD / List > Detail app made with Flask.

## Usage

Once you've cloned the repo, it's just three easy steps:

1. Ensure you have Python, Flask, and SQLite installed
2. Create the SQLite DB (follow `schema.sql`)
   - `sqlite3 my_test_database.db`
   - `CREATE TABLE thing (...);`
3. Run the Flask app
   - `export FLASK_APP=app.py`
   - `export FLASK_ENV=development`
   - `flask run`
