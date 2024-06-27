from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class District(db.Model):
    __tablename__ = 'district'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)     
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable = False)

class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    description = db.Column(db.Text, nullable = False)
    category = db.Column(db.String(50), nullable = False)
    coordinates = db.Column(db.String(50), nullable = False)
    district_id = db.Column(db.Integer, db.ForeignKey('district.id'), nullable = False)
    image_url = db.Column(db.String(255), nullable=False)
    district = db.relationship('District', backref=db.backref('places', lazy=True))


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key = True)
    monday = db.Column(db.Float, nullable=False, default=0.0)
    tuesday = db.Column(db.Float, nullable=False, default=0.0)
    wednesday = db.Column(db.Float, nullable=False, default=0.0)
    thursday = db.Column(db.Float, nullable=False, default=0.0)
    friday = db.Column(db.Float, nullable=False, default=0.0)
    saturday = db.Column(db.Float, nullable=False, default=0.0)
    sunday = db.Column(db.Float, nullable=False, default=0.0)

    attendance = {
    'monday': monday,
    'tuesday': tuesday,
    'wednesday': wednesday,
    'thursday': thursday,
    'friday': friday,
    'saturday': saturday,
    'sunday': sunday
    }
    
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key = True)
    user = review_text = db.Column(db.Text, nullable = False)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable = False)
    review_text = db.Column(db.Text, nullable = False)
    rating = db.Column(db.Integer, nullable = False)
    date = db.Column(db.String(255), nullable = False)
    gender = db.Column(db.String(1), nullable=False) #male or female( "M" / "F")
    image_url = db.Column(db.String(255), nullable=False)
    place = db.relationship('Place', backref = db.backref('reviews', lazy=True))


class Metric(db.Model):
    __tablename__ = 'metrics'
    id = db.Column(db.Integer, primary_key = True)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'), nullable = False)
    review_count = db.Column(db.Integer, nullable = False)
    place = db.relationship('Place', backref = db.backref('metrics', lazy=True))