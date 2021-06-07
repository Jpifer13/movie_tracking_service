from . import BadRequestBody

BAD_REQUEST_ERRORS = (
    BadRequestBody
)


def handle_service_errors(func):
    """
    Exception handler decorator

    Used to remove the need for multiple try except blocks
    """
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except BAD_REQUEST_ERRORS as req_exc:
            data = {'message': str(req_exc)}
            status = 409
            result = data, status
        except Exception as err:
            data = {'message': str(err)}
            status = 500
            result = data, status
        
        data, status = result
        return (data, status)
    
    return wrapper
