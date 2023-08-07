import requests
from bs4 import BeautifulSoup

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.instance_path = os.path.join(os.getcwd(), 'database')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(64))
    grade = db.Column(db.Float())
    rate = db.Column(db.Float())
    link = db.Column(db.String(128))
    img_url = db.Column(db.String(128))
    short_desc = db.Column(db.String())

    def __repr__(self):
        return f"<Movie {self.title}, {self.short_desc}>"

def get_info_from_site():
    data = requests.get('https://movie.daum.net/ranking/reservation')
    soup = BeautifulSoup(data.text, 'html.parser')

    info = soup.select('.list_movieranking > li')
    movie_link_root = 'https://movie.daum.net'
    for i in info :
        title = i.select_one('.link_txt').text
        grade = float(i.select_one('.txt_grade').text)
        rate = i.select_one('.txt_num').text
        rate = float(rate[:len(rate)-1])
        link = i.select_one('.link_txt')['href']
        # full_link = movie_link_root + link
        img_url = i.select_one('.img_thumb')['src']
        short_desc = i.select_one('.link_story').text.strip()
        new_movie = Movie(title=title, grade=grade, rate=rate, link=link, img_url=img_url, short_desc=short_desc)
        db.session.add(new_movie)
    db.session.commit()

@app.route('/list')
def list():
    movies = Movie.query.all()
    return render_template('index.html', movies=movies)

@app.route('/')
def main():
    get_info_from_site()
    return "Success"

if __name__ == "__main__" :
    with app.app_context():
        db.create_all()
    app.run()
    # get_title_rate_reserv()