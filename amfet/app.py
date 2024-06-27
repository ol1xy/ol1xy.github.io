from flask import Flask, render_template, jsonify, send_from_directory, abort
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import District, Place, Review, Metric, db
import os
 # Ваши модели SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
IMAGE_FOLDER = 'static/pictures'
db.init_app(app)

# @app.route('/')
# def main():
#     return render_template('main.html')

# @app.route('/district2')
# def page2():
#     return render_template('2.html')

# @app.route('/')
# def page3():
#     return render_template('3.html')

# Эндпоинт для получения данных о районе, включая места и отзывы
@app.route('/district/<int:district_id>', methods=['GET'])
def district_page(district_id):
    district = District.query.filter_by(id=district_id).first()
    if district:
        places = Place.query.filter_by(district_id=district_id).all()
        reviews = Review.query.join(Place).filter(Place.district_id == district_id).all()
        if district_id == 1:

            return render_template('3.html', district=district, places=places, reviews=reviews)
        if district_id == 2:
            return render_template('2.html', district=district, places=places, reviews=reviews)
        if district_id == 3:
            return render_template('main.html', district=district, places=places, reviews=reviews)


    else:
        return "Район не найден", 404


@app.route('/pictures/<path:filename>', methods=['GET'])

def get_image(filename):
    try:
        return send_from_directory(IMAGE_FOLDER, filename)
    except FileNotFoundError:
        return "File not found", 404

# Эндпоинт для получения всех мест
@app.route('/places', methods=['GET'])
def get_all_places():
    places = Place.query.all()
    return jsonify([{
        'id': place.id,
        'name': place.name,
        'description': place.description,
        'category': place.category,
        'coordinates': place.coordinates,
        'district_id': place.district_id,
        'image_url': place.image_url
    } for place in places])

# Эндпоинт для получения мест по категориям
@app.route('/places/category/<string:category>', methods=['GET'])
def get_places_by_category(category):
    places = Place.query.filter_by(category=category).all()
    return jsonify([{
        'id': place.id,
        'name': place.name,
        'description': place.description,
        'category': place.category,
        'coordinates': place.coordinates,
        'district_id': place.district_id,
        'image_url': place.image_url
    } for place in places])

# Эндпоинт для получения отзывов по оценкам
@app.route('/reviews/rating/<int:rating>', methods=['GET'])
def get_reviews_by_rating(rating):
    reviews = Review.query.filter_by(rating=rating).all()
    return jsonify([{
        'id': review.id,
        'user': review.user,
        'place_id': review.place_id,
        'review_text': review.review_text,
        'rating': review.rating,
        'date': review.date,
        'gender': review.gender,
        'image_url': review.image_url
    } for review in reviews])

# Эндпоинт для получения отзывов по местам
@app.route('/places/<int:place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    reviews = Review.query.filter_by(place_id=place_id).all()
    return jsonify([{
        'id': review.id,
        'user': review.user,
        'place_id': review.place_id,
        'review_text': review.review_text,
        'rating': review.rating,
        'date': review.date,
        'gender': review.gender,
        'image_url': review.image_url
    } for review in reviews])

if __name__ == '__main__':
    app.run(debug=True)

