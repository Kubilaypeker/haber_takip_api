import datetime
import logging
from flask import current_app

from application import create_app
from application.core.utils.log_formatter import NewsLogsFormatter
from application.core.jobs.job_utils import JobUtils


def get_news_from_web():
    app = create_app()
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    with app.app_context():
        today = datetime.datetime.today().strftime("%m/%d/%Y, %H:%M:%S")
        logging.info(f"News scraping started at {today}")
        new_job = JobUtils()
        JobUtils.remove_old_news()
        JobUtils.insert_politic_news(new_job)
        JobUtils.insert_economy_news(new_job)
        JobUtils.insert_tech_news(new_job)
        JobUtils.insert_world_news(new_job)
        JobUtils.insert_magazine_news(new_job)
        JobUtils.insert_sport_news(new_job)

        # TODO other job utils will be calling here



if __name__ == '__main__':
    get_news_from_web()

