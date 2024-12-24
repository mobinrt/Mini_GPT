from .base_exception import BaseError
    
class InvalidCredentialsError(BaseError):
    message = 'Incorrect name or password'