from dataclasses import dataclass
from typing import Optional

from src.app.features.user.domain.user_schema import UserCreate

@dataclass
class CreateUserArgs:
    username: str
    email: str
    password: str

    @classmethod
    def from_pydantic(cls, user_create: UserCreate) -> 'CreateUserArgs':
        return cls(
            username=user_create.username,
            email=user_create.email,
            password=user_create.password
        )

@dataclass
class DisplayUserArgs:
    id: int
    first_name: str
    last_name: str
    email: str
