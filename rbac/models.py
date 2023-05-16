from dataclasses import dataclass, field
from enum import Enum
from uuid import UUID, uuid1

from .exception import Forbidden


class RoleEnum(str, Enum):
    GUEST = "guest"
    ADMIN = "admin"
    EMPLOYEE = "employee"
    MANAGER = "manager"


@dataclass(frozen=False)
class User:
    name: str
    email: str
    role: RoleEnum
    id: UUID = field(default_factory=uuid1)


@dataclass(frozen=False)
class Post:
    user: User
    title: str
    description: str
    id: UUID = field(default_factory=uuid1)
