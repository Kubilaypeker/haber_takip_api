class BaseResponse:
    def __init__(self, is_success=True, message='Success', response_code=200, data=None):
        self.is_success = is_success
        self.message = message
        self.response_code = response_code
        self.data = data
