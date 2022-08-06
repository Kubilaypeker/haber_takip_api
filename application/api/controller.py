from flask import Blueprint, request, jsonify
from flask import current_app

from application.core.app_models import BaseResponse
from application.decorators.api_decorators import require_api_key
from application.core.utils.api_utils import ApiUtils

mod_api = Blueprint('api', __name__, url_prefix='/news/api')


@mod_api.route('/latest', methods=['GET'])

def get_latest_news():
    response = BaseResponse()
    latest_news = ApiUtils.get_latest_news()
    if latest_news:
        response.data = latest_news
    return jsonify(response.__dict__)


@mod_api.route('/politic', methods=['GET'])
@require_api_key
def get_politic_news():
    response = BaseResponse()
    politic_news = ApiUtils.get_politic_news()
    if politic_news:
        response.data = politic_news
    return jsonify(response.__dict__)

@mod_api.route('/world', methods=['GET'])
@require_api_key
def get_world_news():
    response = BaseResponse()
    world_news = ApiUtils.get_world_news()
    if world_news:
        response.data = world_news
    return jsonify(response.__dict__)


@mod_api.route('/economy', methods=['GET'])
@require_api_key
def get_economy_news():
    response = BaseResponse()
    economy_news = ApiUtils.get_economy_news()
    if economy_news:
        response.data = economy_news
    return jsonify(response.__dict__)

@mod_api.route('/magazine', methods=['GET'])
@require_api_key
def get_magazine_news():
    response = BaseResponse
    magazine_news = ApiUtils.get_magazine_news()
    if magazine_news:
        response.data = magazine_news
    return jsonify(response.__dict__)


@mod_api.route('/locald', methods=['GET'])
@require_api_key
def get_local_news():
    pass


@mod_api.route('/tech', methods=['GET'])
@require_api_key
def get_tech_news():
    response = BaseResponse()
    tech_news = ApiUtils.get_tech_news()
    if tech_news:
        response.data = tech_news
    return jsonify(response.__dict__)

@mod_api.route('/sport', methods=['GET'])
@require_api_key
def get_sport_news():
    response = BaseResponse()
    sport_news = ApiUtils.get_sport_news()
    if sport_news:
        response.data = sport_news
    return jsonify(response.__dict__)