from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List
from unittest import TestCase
from common import Permission

from rbac import RoleBasedAccess, Action


class DashboardPermission(Permission):
    def create_allowed_roles(self) -> List[MockEnum]:
        return [MockEnum.Admin, MockEnum.User]

    def read_allowed_roles(self) -> List[MockEnum]:
        return [MockEnum.All]

    def update_allowed_roles(self) -> List[MockEnum]:
        return [MockEnum.Admin, MockEnum.User]

    def delete_allowed_roles(self) -> List[MockEnum]:
        return [MockEnum.Admin]


class MockEnum(str, Enum):
    Admin = "admin"
    User = "user"
    Guest = "guest"
    All = "*"


@dataclass(frozen=True)
class MockUser:
    name: str
    role: MockEnum


class TestPermission(TestCase):
    def test_admin_create_dashboard(self):
        rbac = RoleBasedAccess[MockEnum]()
        bob = MockUser(name="bob", role=MockEnum.Admin)

        is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.CREATE)

        self.assertEqual(is_allowed, True)

    def test_guest_read_dashboard(self):
        rbac = RoleBasedAccess[MockEnum]()
        bob = MockUser(name="bob", role=MockEnum.Guest)

        is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.READ)

        self.assertEqual(is_allowed, True)
