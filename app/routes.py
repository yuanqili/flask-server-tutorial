from pprint import pprint

from flask import render_template, request

from app import app
from app.models import Post
from app.utils.weather import get_city_7d_weather


@app.route('/', methods=['GET'])
def index():
    username = request.args.get('username', 'stranger', type=str)
    show_detail = request.args.get('show_detail', False, type=bool)
    posts = Post.query.all()
    return render_template('index.html', username=username, show_detail=show_detail, posts=posts)


@app.route('/weather', methods=['GET'])
def query():
    city = request.args.get('city', '南京', type=str)
    pprint(city)
    data = get_city_7d_weather(city)
    pprint(data)
    return render_template('weather.html', city=city, data=data)
