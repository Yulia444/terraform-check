from flask import render_template, url_for, request, redirect
from app import app
from app.models import Image, Dish, Review, News, SubscribeForNews
from app import db
from app.forms import SendReview, Subscribe
from sqlalchemy import desc

navies = ['gallery', 'menu', 'news', 'reviews']


@app.route('/', methods=['GET', 'POST'])
def main():
    form = Subscribe()
    if request.method == 'POST':
        subscriber = SubscribeForNews(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template("main.html", navies=navies, form=form)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    form = Subscribe()
    if form.validate_on_submit():
        subscriber = SubscribeForNews(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        return redirect(url_for('gallery'))
    images = Image.query.filter(Image.link.contains('gallery')).all()
    return render_template("gallery.html", images=images, navies=navies,
                           form=form)


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    form = Subscribe()
    if form.validate_on_submit():
        subscriber = SubscribeForNews(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        return redirect(url_for('menu'))
    dishes = Dish.query.all()
    categories = list(set(dish.dish_type for dish in Dish.query.all()))
    return render_template("menu.html", dishes=dishes, categories=categories,
                           navies=navies, form=form)


@app.route('/menu/<string:category>', methods=['GET', 'POST'])
def menu_category(category):
    form = Subscribe()
    if form.validate_on_submit():
        subscriber = SubscribeForNews(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        return redirect(url_for('menu_category'))
    dishes = Dish.query.filter_by(dish_type=category).all()
    categories = set(dish.dish_type for dish in Dish.query.all())
    return render_template("menu.html", dishes=dishes, categories=categories,
                           navies=navies, form=form)


@app.route('/news')
def news():
    news = News.query.order_by(News.id.desc())
    return render_template("news.html", news=news, navies=navies)


@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    reviews = Review.query.order_by(Review.id.desc())
    form = SendReview()
    if request.method == 'POST':
        author = form.author.data
        title = form.title.data
        review = form.review.data
        new_review = Review(title=title, author=author, review=review)
        db.session.add(new_review)
        db.session.commit()
        return redirect(url_for('reviews'))
    return render_template("reviews.html", navies=navies, reviews=reviews,
                           form=form)

