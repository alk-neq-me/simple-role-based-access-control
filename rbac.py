from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from abc import ABC, abstractmethod
from typing import List
import logging


class Authoritor(ABC):
    """trait authoritor"""
    @abstractmethod
    def is_authorized(self, permission: Permission, role: Role, action: Action) -> bool:
        """check is authorize, return bool"""


class Permission(ABC):
    """trait action creator"""
    @abstractmethod
    def create_allowed_roles(self) -> List[Role]:
        """create read allowed roles, list"""

    @abstractmethod
    def read_allowed_roles(self) -> List[Role]:
        """read read allowed roles, list"""

    @abstractmethod
    def update_allowed_roles(self) -> List[Role]:
        """update read allowed roles, list"""

    @abstractmethod
    def delete_allowed_roles(self) -> List[Role]:
        """delete read allowed roles, list"""


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"
    ALL = "*"


class Action(str, Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"


@dataclass(frozen=True)
class User:
    name: str
    role: Role


@dataclass(frozen=True)
class Rbac(Authoritor):
    def is_authorized(self, permission: Permission, role: Role, action: Action) -> bool:
        access = False
        perm: List[Role] = []

        match action:
            case Action.CREATE:
                logging.info("add create")
                perm.extend(permission.create_allowed_roles())
            case Action.READ:
                logging.info("add read")
                perm.extend(permission.read_allowed_roles())
            case Action.UPDATE:
                logging.info("add update")
                perm.extend(permission.update_allowed_roles())
            case Action.DELETE:
                logging.info("add delete")
                perm.extend(permission.delete_allowed_roles())
            case _:
                raise Exception("Unreachable")

        logging.info(f"{perm = }")

        if Role.ALL in perm:
            access = True
        elif role in perm:
            access = True

        return access


@dataclass(frozen=True)
class DashboardPermission(Permission):
    def create_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ADMIN, Role.USER]
        return allowed_roles

    def read_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ALL]
        return allowed_roles

    def update_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ADMIN, Role.USER]
        return allowed_roles

    def delete_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ADMIN]
        return allowed_roles


def main():
    logging.basicConfig(
        format="[  ] %(message)s", 
        datefmt="%Y-%m-%d",
        level=logging.WARN
    )
    rbac = Rbac()

    user = User(name="bob", role=Role.GUEST)

    is_allowed = rbac.is_authorized(
        permission=DashboardPermission(), 
        role=user.role, 
        action=Action.UPDATE
    )

    print(is_allowed)


if __name__ == "__main__":
    main()
