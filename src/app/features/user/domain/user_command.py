from dataclasses import dataclass
from typing import Optional

@dataclass
class CreateUserArgs:
    username: str
    email: str
    password: str


@dataclass
class DisplayUserArgs:
    id: int
    first_name: str
    last_name: str
    email: str
