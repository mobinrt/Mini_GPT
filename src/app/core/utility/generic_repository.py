from typing import Type, TypeVar, Sequence, Optional
from datetime import datetime

from src.app.core.config.model.base_model import BaseModel
from app.core.abs.abs_repository import BaseRepository

TModel = TypeVar('TModel', bound=BaseModel)

class GenericRepository(BaseRepository[TModel]):
    def __init__(self, model: Type[TModel]) -> None:
        self.model = model

    async def create(self, entity: TModel) -> TModel:
        return entity

    async def find_by_email(self, email: str) -> Optional[TModel]:
        return await self.model.get_or_none(email=email)

    async def find_all(self) -> Sequence[TModel]:
        return await self.model.all()

    async def update(self, second_state: TModel, first_state: TModel) -> TModel:
        for var, value in vars(second_state).items():
            setattr(first_state, var, value)
        first_state.updated_at = datetime.now()
        return first_state

    async def delete(self, entity: TModel) -> Optional[TModel]:
        return entity
