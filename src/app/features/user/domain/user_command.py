from dataclasses import dataclass

from src.app.features.user.domain.user_schema import UserCreate, GetUserByID

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
class GetUserByIDArgs:
    id: int
    
    @classmethod
    def from_pydantic(cls, get_user: GetUserByID) -> 'GetUserByIDArgs':
        return cls(
            id=get_user.id,
        )
    