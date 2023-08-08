import requests
from bs4 import BeautifulSoup

import os
import datetime
import uuid
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.instance_path = os.path.join(os.getcwd(), 'database')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.String(64), primary_key=True)
    title = db.Column(db.String(64))
    link = db.Column(db.String(128))
    img_url = db.Column(db.String(128))
    short_desc = db.Column(db.String())
    DailyRankingR = db.relationship('DailyRanking', backref='movie')

    def __repr__(self):
        return f"<Movie {self.title}, {self.short_desc}>"

class DailyRanking(db.Model) :
    __tablename__ = "dailyranking"
    id = db.Column(db.String(64), primary_key=True)
    date = db.Column(db.String(16))
    grade = db.Column(db.Float())
    rate = db.Column(db.Float())
    movieid = db.Column(db.String(64), db.ForeignKey('movie.id'))
    ranking = db.Column(db.Integer())

def get_info_from_site():
    data = requests.get('https://movie.daum.net/ranking/reservation')
    soup = BeautifulSoup(data.text, 'html.parser')

    info = soup.select('.list_movieranking > li')
    movie_link_root = 'https://movie.daum.net'
    ranking = 0
    for i in info :
        ranking += 1
        title = i.select_one('.link_txt').text
        grade = float(i.select_one('.txt_grade').text)
        rate = i.select_one('.txt_num').text
        rate = float(rate.replace('%', ''))
        link = i.select_one('.link_txt')['href']
        # full_link = movie_link_root + link
        img_url = i.select_one('.img_thumb')['src']
        short_desc = i.select_one('.link_story').text.strip()

        movie = Movie.query.filter_by(title=title).all()
        if not movie:
            new_movie = Movie(id=str(uuid.uuid4()), title=title, link=link, img_url=img_url, short_desc=short_desc)
            db.session.add(new_movie)
        movie = Movie.query.filter_by(title=title).one()
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        new_ranking = DailyRanking(id=str(uuid.uuid4()), date=today, grade=grade, rate=rate, movieid=movie.id, ranking=ranking)
        db.session.add(new_ranking)
    db.session.commit()

@app.route('/list/')
def list():
    date = request.args.get('date', default=1, type=str)
    movies = db.session.query(DailyRanking.ranking, Movie.title, Movie.short_desc, Movie.link, Movie.img_url, DailyRanking.grade, DailyRanking.rate) \
            .join(DailyRanking, DailyRanking.movieid == Movie.id) \
            .filter(DailyRanking.date == date) \
            .order_by(DailyRanking.ranking) \
            .all()
    return render_template('index.html', date=date, movies=movies)

@app.route('/daily_ranking')
def daily_ranking():
    dates = db.session.query(DailyRanking.date.distinct()).all()
    print(dates)
    return render_template('datelist.html', dates=dates)

@app.route('/get_data')
def main():
    get_info_from_site()
    return "Success"

if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run()