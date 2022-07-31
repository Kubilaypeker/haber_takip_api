import datetime
import re

import requests
from flask import current_app
from bs4 import BeautifulSoup

from application.core.enums import URL_SUFFIX, NewsCategories
from application.core.models import NEWS
from application import db

CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')


class JobUtils:
    def __init__(self):
        self.url_prefix = current_app.config.get("URL_PREFIX")

    @staticmethod
    def cleanhtml(raw_html):
        cleantext = re.sub(CLEANR, '', raw_html)
        return cleantext

    @staticmethod
    def extract_news_content(url):
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html5lib")
        news_wrapper = soup.find("div", "wrapper detay-v3_3 haber_metni pad-bot-20")
        news_content = ""
        if news_wrapper:
            news_wrapper = news_wrapper.find_all("p")
            for paragraph in news_wrapper:
                if paragraph.text:
                    news_content += paragraph.text + "\n\r\n\r"
            news_content = JobUtils.cleanhtml(news_content)
        return news_content

    @staticmethod
    def remove_old_news():
        three_day_ago = datetime.datetime.utcnow() - datetime.timedelta(days=3)
        old_news_records = NEWS.query.filter(NEWS.insert_date > three_day_ago).all()
        for old_news in old_news_records:
            db.session.delete(old_news)
        db.session.commit()

    @staticmethod
    def parse_news_content(requested_url, url_prefix):
        request = requests.get(requested_url)
        soup = BeautifulSoup(request.content, "html5lib")
        politic_news_list = soup.find("ul", "news-list").find_all("li", "nws")
        parsed_news_list = []
        for news in politic_news_list[:20]:
            news_content_item = news.find("a", "content")
            news_template = {
                "news_date": news.find("span", "data_calc").attrs.get("title", ""),
                "news_photo": news.find("a", "fr").find("img", "lazy").attrs.get("src"),
                "news_title": news.find("a", "content").attrs.get("title"),
                "news_preview_content": news.find("p", "news-detail news-column").text,
                "news_content": JobUtils.extract_news_content(url_prefix + news_content_item.attrs.get("href"))
            }
            parsed_news_list.append(news_template)
        return parsed_news_list

    @staticmethod
    def insert_records(data_list, category):
        record_list = []
        for data in data_list:
            news_query = NEWS.query.filter(NEWS.news_title == data['news_title']).first()
            if not news_query:
                new_politic_record = NEWS(
                    news_date=data["news_date"],
                    news_photo=data["news_photo"],
                    news_title=data["news_title"],
                    news_preview_content=data["news_preview_content"],
                    news_content=data["news_content"],
                    news_category=category,
                    insert_date=datetime.datetime.utcnow())
                record_list.append(new_politic_record)
        db.session.bulk_save_objects(record_list)
        db.session.commit()

    def insert_politic_news(self):
        category = NewsCategories.POLITIC.value
        requested_url = self.url_prefix + URL_SUFFIX.POLITIC.value
        parsed_politic_news = JobUtils.parse_news_content(requested_url=requested_url, url_prefix=self.url_prefix)
        JobUtils.insert_records(parsed_politic_news, category)

    def insert_tech_news(self):
        category = NewsCategories.TECH.value
        requested_url = self.url_prefix + URL_SUFFIX.TECH.value
        parsed_tech_news = JobUtils.parse_news_content(requested_url=requested_url, url_prefix=self.url_prefix)
        JobUtils.insert_records(parsed_tech_news, category)

    def insert_world_news(self):
        category = NewsCategories.WORLD.value
        requested_url = self.url_prefix + URL_SUFFIX.WORLD.value
        parsed_tech_news = JobUtils.parse_news_content(requested_url=requested_url, url_prefix=self.url_prefix)
        JobUtils.insert_records(parsed_tech_news, category)

    def insert_economy_news(self):
        category = NewsCategories.ECONOMY.value
        requested_url = self.url_prefix + URL_SUFFIX.ECONOMY.value
        parsed_economy_news = JobUtils.parse_news_content(requested_url=requested_url, url_prefix=self.url_prefix)
        JobUtils.insert_records(parsed_economy_news, category)

    def insert_magazine_news(self):
        category = NewsCategories.MAGAZINE.value
        requested_url = self.url_prefix + URL_SUFFIX.MAGAZINE.value
        parsed_magazine_news = JobUtils.parse_news_content(requested_url=requested_url, url_prefix=self.url_prefix)
        JobUtils.insert_records(parsed_magazine_news, category)

