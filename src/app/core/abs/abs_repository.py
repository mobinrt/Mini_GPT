from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic, Optional

_T = TypeVar('_T')


class BaseRepository(ABC, Generic[_T]):
    @abstractmethod
    async def create(self, entity: _T):
        raise NotImplementedError()

    @abstractmethod
    async def find_all(self) -> Sequence[_T]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[_T]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, id: int) -> Optional[_T]:
        raise NotImplementedError()

            
    @abstractmethod
    async def update(self, second_state: _T, first_state: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    async def delete(self, entity: _T) -> Optional[_T]:
        raise NotImplementedError()
