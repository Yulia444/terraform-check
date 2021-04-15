from app import db
from app import app
from flask import redirect, url_for
from app.models import Image, Dish, Review, News, SubscribeForNews
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose, Admin
from app.forms import SendLetterToSubscribers
from flask_ckeditor import CKEditorField
from app import mail
from flask_mail import Message


class SendLetter(BaseView):
    @expose('/', methods=['GET', 'POST'])
    def sendletter(self):
        form = SendLetterToSubscribers()
        if form.validate_on_submit():
            recipients = [sub.email for sub in SubscribeForNews.query.all()]
            msg = Message(form.subject.data, recipients=recipients)
            msg.html = form.summernote.data
            mail.send(msg)
            return redirect(url_for('sendletter.sendletter'))
        return self.render("admin/send_letter.html", form=form)


class NewsEdit(ModelView):
    form_overrides = dict(data=CKEditorField)
    create_template = 'edit.html'
    edit_template = 'edit.html'


admin = Admin(app, template_mode='bootstrap3')
admin.add_view(ModelView(Image, db.session))
admin.add_view(ModelView(Dish, db.session))
admin.add_view(ModelView(Review, db.session))
admin.add_view(ModelView(SubscribeForNews, db.session, name='Subscribers'))
admin.add_view(SendLetter('Send letter', url='/sendletter'))
admin.add_view(NewsEdit(News, db.session))
