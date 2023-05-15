from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Dict
from enum import Enum

from exception import NotFoundRole


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


@dataclass(frozen=True)
class Role:
    name: RoleEnum
    permissions: List[Permission]


@dataclass(frozen=True)
class Permission:
    resource: str
    action: str

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
                Permission("*", "!"),
                # Permission("dashboard", "read")
            ]),
            RoleEnum.ADMIN: Role(RoleEnum.ADMIN, [Permission("*", "*")]),
            RoleEnum.EMPLOYEE: Role(RoleEnum.EMPLOYEE, [
                Permission("dashboard", "read"),
                Permission("posts", "*"),
            ]),
            RoleEnum.MANAGER: Role(RoleEnum.MANAGER, [
                Permission("posts", "*"),
                Permission("dashboard", "read"),
                Permission("employee", "*")
            ]),
        }
    
    def get_role(self, role: RoleEnum) -> Role:
        return self.access_rules.get(role, self.access_rules[RoleEnum.GUEST])

    def add_access_rule(self, role: RoleEnum, permission: Permission) -> None:
        if role not in self.access_rules:
            raise NotFoundRole(f"Not Found Role name with {role}")
        self.access_rules[role].permissions.append(permission)

    def authorize(self, user: User, permission: str) -> bool:
        access = False
        for access_rule in self.access_rules.values():
            if access_rule.name == user.role:
                for perm in access_rule.permissions:
                    resource, action = permission.split(":")
                    print(permission, perm)
                    if (resource == perm.resource or perm.resource == "*") and (action == perm.action or (perm.action == "*" and not perm.action == "!")):
                        access = True
                    if (resource == perm.resource and perm.action == "!"):
                        access = False
        return access
