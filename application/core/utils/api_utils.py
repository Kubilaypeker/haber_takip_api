import json

from application.core.models import NEWS
from application.core.enums import NewsCategories


class ApiUtils:
    @staticmethod
    def get_latest_news():
        news_list = []
        for index,category in enumerate(NewsCategories, start = 1):
            news_records = NEWS.query.filter(NEWS.news_category == category.value).order_by(NEWS.insert_date.desc()).limit(4).all()
            if news_records:
                news_list.extend(news_records)
        return ApiUtils.serialize_news(news_list)



    @staticmethod
    def get_politic_news():
        news_records = NEWS.query.filter(NEWS.news_category == NewsCategories.POLITIC.value).all()
        return ApiUtils.serialize_news(news_records)

    @staticmethod
    def get_world_news():
        news_records = NEWS.query.filter(NEWS.news_category == NewsCategories.WORLD.value).all()
        return ApiUtils.serialize_news(news_records)

    @staticmethod
    def get_economy_news():
        news_records = NEWS.query.filter(NEWS.news_category == NewsCategories.ECONOMY.value).all()
        return ApiUtils.serialize_news(news_records)

    @staticmethod
    def get_magazine_news():
        news_records = NEWS.query.filter(NEWS.news_category == NewsCategories.MAGAZINE.value).all()
        return ApiUtils.serialize_news(news_records)


    @staticmethod
    def get_local_news():
        pass

    @staticmethod
    def get_tech_news():
        news_records = NEWS.query.filter(NEWS.news_category == NewsCategories.TECH.value).all()
        return ApiUtils.serialize_news(news_records)

    def get_sport_news(self):
        news_records = NEWS.query.filter(NEWS.news_category == NewsCategories.SPORT.value).all()
        return ApiUtils.serialize_news(news_records)


    @staticmethod
    def serialize_news(news_records):
        news_records_list = []
        for news in news_records:
            news_template = {
                "news_date": news.news_date,
                "news_photo": news.news_photo,
                "news_title": news.news_title,
                "news_preview_content": news.news_preview_content,
                "news_content": news.news_content
            }
            news_records_list.append(news_template)
        return news_records_list
