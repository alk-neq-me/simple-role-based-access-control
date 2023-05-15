from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum

from exception import FailedPermission, NotFoundRole


@dataclass(frozen=True)
class User:
    name: str
    email: str
    role: RoleEnum


class RoleEnum(str, Enum):
    GUEST = "guest"
    ADMIN = "admin"
    EMPLOYEE = "employee"
    MANAGER = "manager"


class ActionEnum(str, Enum):
    READ = "read"
    UPDATE = "update"
    CREATE = "create"
    DELETE = "delete"
    ALOWED = "*"
    DENIED = "!"


@dataclass(frozen=True)
class Role:
    name: RoleEnum
    permissions: List[Permission]


@dataclass(frozen=True)
class Permission:
    resource: str
    action: ActionEnum

    @property
    def name(self) -> str:
        return f"{self.resource}:{self.action}"


@dataclass(frozen=False)
class AccessRule:
    """Role-Based Access Control"""

    access_rules: Dict[RoleEnum, Role] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.access_rules = {
            RoleEnum.GUEST: Role(RoleEnum.GUEST, [
                Permission("*", ActionEnum.DENIED),
                Permission("posts", ActionEnum.READ),
                # Permission("dashboard", "read")
            ]),
            RoleEnum.ADMIN: Role(RoleEnum.ADMIN, [Permission("*", ActionEnum.ALOWED)]),
            RoleEnum.EMPLOYEE: Role(RoleEnum.EMPLOYEE, [
                Permission("dashboard", ActionEnum.READ),
                Permission("posts", ActionEnum.ALOWED),
            ]),
            RoleEnum.MANAGER: Role(RoleEnum.MANAGER, [
                Permission("posts", ActionEnum.ALOWED),
                Permission("dashboard", ActionEnum.READ),
                Permission("employee", ActionEnum.ALOWED)
            ]),
        }
    
    def get_role(self, role: RoleEnum) -> Role:
        return self.access_rules.get(role, self.access_rules[RoleEnum.GUEST])

    def add_access_rule(self, role: RoleEnum, permission: Permission) -> None:
        if role not in self.access_rules:
            raise NotFoundRole(f"Not Found Role name with {role}")
        self.access_rules[role].permissions.append(permission)

    def authorize(self, user: User, permission: str, log: bool = True) -> bool:
        access = False
        resource, action = permission.split(":")
        if not action in list(ActionEnum):
            raise FailedPermission(f"Not defined `{action}`, you must use create, read, update, delete!")
        for access_rule in self.access_rules.values():
            if access_rule.name == user.role:
                for perm in access_rule.permissions:
                    if log:
                        print(permission, perm)
                    if (resource == perm.resource or perm.resource == "*") and (action == perm.action or (perm.action == "*" and not perm.action == "!")):
                        access = True
                    if (resource == perm.resource and perm.action == "!"):
                        access = False
        return access
