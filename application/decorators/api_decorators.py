from functools import wraps

from flask import current_app
from flask import request, abort, make_response


def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if request.args.get('key') == current_app.config.get('API_KEY'):
            return f(*args, **kwargs)
        else:
            current_app.logger.exception('Unauthorized Access ')
            abort(make_response("Unauthorized Access to use API", 401))

    return decorated
