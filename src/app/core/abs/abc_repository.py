from abc import ABC, abstractmethod
from typing import TypeVar, Sequence, Generic

_T = TypeVar('_T')


class BaseRepository(ABC, Generic[_T]):
    @abstractmethod
    async def create(self, model: _T):
        raise NotImplementedError()

    @abstractmethod
    async def find_all(self) -> Sequence[_T]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_id(self, id: int) -> _T | None:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, second_state: _T, first_state: _T) -> _T:
        raise NotImplementedError()

    @abstractmethod
    async def delete_by_id(self, id: int) -> None:
        raise NotImplementedError()
