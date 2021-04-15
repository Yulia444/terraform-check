from app import db
import datetime


class Image(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(48))


class Dish(db.Model):
    __tablename__ = 'dishes'

    id = db.Column(db.Integer, primary_key=True)
    picture = db.Column(db.String(48))
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    dish_type = db.Column(db.Enum('appetizers', 'salads', 'pasta & rissoto',
                                  'seafood', 'from the grill',
                                  'main dishes', 'desserts', 'drink',
                                  name='dish_type'), default='seafood')


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(16))
    title = db.Column(db.String(72))
    review = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow())


class SubscribeForNews(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
