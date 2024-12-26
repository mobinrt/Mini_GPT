from abc import ABC
from typing import Sequence, TypeVar, Generic

from src.app.core.config.model.base_model import BaseModel

_Model = TypeVar('_Model', bound=BaseModel)

class BaseService(ABC, Generic[_Model]):
    pass