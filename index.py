from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import UploadForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '[\x8fb\xf2\xcbN\x8a\x05J\x12^LP\xf4\xfa\xbb\xa34+\xab\xc1\xb3(\x7f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gaming_zone.db'

db = SQLAlchemy(app)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_title = db.Column(db.String(20), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    games_posts = db.relationship('Games_posts', backref='individual_games', lazy=True)

    

class Games_posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), unique=True, nullable=False)
    content = db.Column(db.String(10000), unique=True, nullable=False)
    descriptors = db.Column(db.String(150), unique=False, nullable=True)
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/xbox/games', methods=['GET', 'POST'])
def xbox_games():
    form = UploadForm()
    if form.validate_on_submit():
        print("Upload successful")
        return redirect(url_for('xbox_games'))
    return render_template('individual_games.html', title='Upload', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
