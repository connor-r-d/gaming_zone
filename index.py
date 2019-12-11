import ConfigParser

from flask import Flask, g, render_template, url_for, redirect, request
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
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=2")
    mass_effect = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=4")
    halo = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=5")
    witcher = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=6")
    dark_souls = cur.fetchall();
    return render_template('xbox_games.html', mass_effect=mass_effect, halo=halo, witcher=witcher, dark_souls=dark_souls)

@app.route('/playstation', methods=['GET', 'POST'])
def playstation_games():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=1")
    the_last = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=2")
    mass_effect = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=5")
    witcher = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=6")
    dark_souls = cur.fetchall();

    return render_template('playstation_games.html', the_last=the_last, mass_effect=mass_effect, witcher=witcher, dark_souls=dark_souls)

@app.route('/nintendo', methods=['GET', 'POST'])
def nintendo_games():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=3")
    the_legend = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=5")
    witcher = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=6")
    dark_souls = cur.fetchall();
    return render_template('nintendo_games.html', the_legend=the_legend, witcher=witcher, dark_souls=dark_souls)

@app.route('/pc', methods=['GET', 'POST'])
def pc_games():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=2")
    mass_effect = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=5")
    witcher = cur.fetchall();

    cur.execute("SELECT * FROM games WHERE id=6")
    dark_souls = cur.fetchall();
    return render_template('pc.html', mass_effect=mass_effect, witcher=witcher, dark_souls=dark_souls)

@app.route('/games/the_last_of_us', methods=['GET', 'POST'])
def the_last_of_us():
    db = get_db()
    db.cursor().execute('INSERT INTO games values (1, "The Last of Us", "ps4")')
    db.cursor().execute('INSERT INTO games values (2, "Mass Effect", "three")')
    db.cursor().execute('INSERT INTO games values (3, "The Legend of Zelda", "nintendo")')
    db.cursor().execute('INSERT INTO games values (4, "Halo Infinite", "xbox")')
    db.cursor().execute('INSERT INTO games values (5, "Witcher 3", "four")')
    db.cursor().execute('INSERT INTO games values (6, "Dark Souls", "four")')
    db.cursor().execute('INSERT INTO lastDatabase values ("Fighting the end boss", "To fight the end boss", "End Boss Fight")')
    db.cursor().execute('INSERT INTO massDatabase values ("Fighting the end boss", "To fight the end boss", "End Boss Fight")')
    db.cursor().execute('INSERT INTO thelegendDatabase values ("Fighting the end boss", "To fight the end boss", "End Boss Fight")')
    db.cursor().execute('INSERT INTO haloDatabase values ("Fighting the end boss", "To fight the end boss", "End Boss Fight")')
    db.cursor().execute('INSERT INTO witcherDatabase values ("Fighting the end boss", "To fight the end boss", "End Boss Fight")')
    db.cursor().execute('INSERT INTO darkDatabase values ("Fighting the end boss", "To fight the end boss", "End Boss Fight")')
    db.commit()

    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=1")
    the_last = cur.fetchall();
    
    if request.method == 'POST':
            titl = request.form['titl']
            cont = request.form['cont']
            desc = request.form['desc']
            db = get_db()
            db.cursor().execute("INSERT INTO lastDatabase (title,content,descriptors) VALUES (?,?,?)",(titl,cont,desc) )
            db.commit()
            return redirect(url_for('the_last_of_us'));
           
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM lastDatabase")
    the_last_posts = cur.fetchall();

    return render_template('the_last_of_us.html', the_last=the_last, the_last_posts=the_last_posts)


@app.route('/games/mass_effect', methods=['GET', 'POST'])
def mass_effect():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=2")
    mass_effect = cur.fetchall();
    
    if request.method == 'POST':
            titl = request.form['titl']
            cont = request.form['cont']
            desc = request.form['desc']
            db = get_db()
            db.cursor().execute("INSERT INTO massDatabase (title,content,descriptors) VALUES (?,?,?)",(titl,cont,desc) )
            db.commit()
            return redirect(url_for('mass_effect'));
           
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM massDatabase")
    mass_effect_posts = cur.fetchall();

    return render_template('mass_effect.html', mass_effect=mass_effect, mass_effect_posts=mass_effect_posts)

@app.route('/games/the_legend_of_zelda', methods=['GET', 'POST'])
def the_legend_of_zelda():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=3")
    the_legend = cur.fetchall();
    
    if request.method == 'POST':
            titl = request.form['titl']
            cont = request.form['cont']
            desc = request.form['desc']
            db = get_db()
            db.cursor().execute("INSERT INTO thelegendDatabase (title,content,descriptors) VALUES (?,?,?)",(titl,cont,desc) )
            db.commit()
            return redirect(url_for('the_legend_of_zelda'));
           
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM thelegendDatabase")
    the_legend_posts = cur.fetchall();

    return render_template('the_legend.html', the_legend=the_legend, the_legend_posts=the_legend_posts)

@app.route('/games/halo_infinite', methods=['GET', 'POST'])
def halo_infinite():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=4")
    halo = cur.fetchall();
    
    if request.method == 'POST':
            titl = request.form['titl']
            cont = request.form['cont']
            desc = request.form['desc']
            db = get_db()
            db.cursor().execute("INSERT INTO haloDatabase (title,content,descriptors) VALUES (?,?,?)",(titl,cont,desc) )
            db.commit()
            return redirect(url_for('halo_infinite'));
           
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM haloDatabase")
    halo_posts = cur.fetchall();

    return render_template('halo.html', halo=halo, halo_posts=halo_posts)

@app.route('/games/witcher_3', methods=['GET', 'POST'])
def witcher_3():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=5")
    witcher = cur.fetchall();
    
    if request.method == 'POST':
            titl = request.form['titl']
            cont = request.form['cont']
            desc = request.form['desc']
            db = get_db()
            db.cursor().execute("INSERT INTO witcherDatabase (title,content,descriptors) VALUES (?,?,?)",(titl,cont,desc) )
            db.commit()
            return redirect(url_for('witcher_3'));
           
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM witcherDatabase")
    witcher_posts = cur.fetchall();

    return render_template('witcher.html', witcher=witcher, witcher_posts=witcher_posts)

@app.route('/games/dark_souls', methods=['GET', 'POST'])
def dark_souls():
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM games WHERE id=6")
    dark_souls = cur.fetchall();
    
    if request.method == 'POST':
            titl = request.form['titl']
            cont = request.form['cont']
            desc = request.form['desc']
            db = get_db()
            db.cursor().execute("INSERT INTO darkDatabase (title,content,descriptors) VALUES (?,?,?)",(titl,cont,desc) )
            db.commit()
            return redirect(url_for('dark_souls'));
           
    con = sql.connect("var/gaming_zone.db")
    con.row_factory = sql.Row

    cur = con.cursor()

    cur.execute("SELECT * FROM darkDatabase")
    dark_souls_posts = cur.fetchall();

    return render_template('dark_souls.html', dark_souls=dark_souls, dark_souls_posts=dark_souls_posts)

@app.route('/config/')
def config():
    s = []
    s.append('debug:'+app.config['DEBUG'])
    s.append('port:'+app.config['port'])
    s.append('url:'+app.config['url'])
    s.append('ip_address:'+app.config['ip_address'])
    return ', '.join(s)

def init(app):
    config = ConfigParser.ConfigParser()
    try:
        config_location = "etc/defaults.cfg"
        config.read(config_location)
        
        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
    except:
        print "Could not read configs from: ", config_location

if __name__ == '__main__':
    init(app)
    app.run(
        host=app.config['ip_address']
        port=int(app.config['port']))
        
        
        
        
        










