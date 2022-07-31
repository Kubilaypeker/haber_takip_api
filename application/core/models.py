from application import db


class NEWS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    news_date = db.Column(db.String(50))
    news_photo = db.Column(db.String)
    news_title = db.Column(db.String)
    news_preview_content = db.Column(db.String)
    news_content = db.Column(db.String)
    news_category = db.Column(db.String)
    insert_date = db.Column(db.DateTime)
