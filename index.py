from flask import Flask, g, render_template, url_for, redirect
import sqlite3 as sql

from flask import Flask
app = Flask(__name__)
db_location = 'var/gaming_zone.db'

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sql.connect(db_location)
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
    #db = get_db()
    #db.cursor().execute('insert into games values (1, "The Last of Us", "ps4")')
    #db.cursor().execute('insert into games values (2, "Mass effect", "three")')
    #db.cursor().execute('insert into games values (3, "The legend of Zelda", "switch")')
    #db.cursor().execute('insert into games values (4, "Halo Infinite", "xbox")')
    #db.cursor().execute('insert into games values (5, "Witcher 3", "four")')
    #db.cursor().execute('insert into games values (6, "Dark Souls", "four")')
    #db.commit()

    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=1")
    the_last = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=2")
    mass_effect = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=3")
    the_legend = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=4")
    halo = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=5")
    witcher = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=6")
    dark_souls = cur.fetchall();

    return render_template('index.html', the_last=the_last, mass_effect=mass_effect, the_legend=the_legend, halo=halo, witcher=witcher, dark_souls=dark_souls)

@app.route('/xbox', methods=['GET', 'POST'])
def xbox_games():
    return render_template('xbox_games.html')

@app.route('/playstation', methods=['GET', 'POST'])
def playstation_games():
    return render_template('playstation_games.html')

@app.route('/nintendo', methods=['GET', 'POST'])
def nintendo_games():
    return render_template('nintendo_games.html')

@app.route('/pc', methods=['GET', 'POST'])
def pc_games():
    return render_template('pc.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
