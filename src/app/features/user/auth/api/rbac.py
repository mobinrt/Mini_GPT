from src.app.core.exception.base_exception import BaseError

from functools import wraps

def role_required(required_role: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            Authorize = kwargs.get('Authorize')
            Authorize.jwt_required()
            role = Authorize.get_raw_jwt().get('role')
            if role != required_role:
                raise BaseError('Access forbidden')
            return await func(*args, **kwargs)
        return wrapper
    return decorator
