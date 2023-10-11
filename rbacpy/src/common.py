from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class Authoritor(ABC):
    """trait authoritor"""
    @abstractmethod
    def is_authorized(self, permission: Permission, role: str, action: Action) -> bool:
        """check is authorize, return bool"""


class Permission(ABC):
    """trait action creator"""
    @abstractmethod
    def create_allowed_roles(self) -> List[str]:
        """create read allowed roles, list"""

    @abstractmethod
    def read_allowed_roles(self) -> List[str]:
        """read read allowed roles, list"""

    @abstractmethod
    def update_allowed_roles(self) -> List[str]:
        """update read allowed roles, list"""

    @abstractmethod
    def delete_allowed_roles(self) -> List[str]:
        """delete read allowed roles, list"""


# class Role(str, Enum):
#     ADMIN = "admin"
#     USER = "user"
#     GUEST = "guest"
#     ALL = "*"


class Action(str, Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"

