from flask import Flask, g, render_template, url_for, redirect
import sqlite3 as sql

from flask import Flask
app = Flask(__name__)
db_location = 'var/gaming_zone.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
    return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.route('/')
def home():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM games")
    rows = cur.fetchall();
    return render_template('index.html', rows = rows)

@app.route('/xbox/games', methods=['GET', 'POST'])
def xbox_games():
    return render_template('individual_games.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
