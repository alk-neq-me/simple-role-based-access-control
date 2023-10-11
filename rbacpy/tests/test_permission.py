from dataclasses import dataclass
from enum import Enum
from unittest import TestCase

from rbac import RoleBasedAccess, Action
from permissions.dashboard import DashboardPermission


class MockEnum(str, Enum):
    Admin = "admin"
    User = "user"
    Guest = "guest"


@dataclass(frozen=True)
class MockUser:
    name: str
    role: MockEnum


class TestPermission(TestCase):
    def test_admin_create_dashboard(self):
        rbac = RoleBasedAccess()
        bob = MockUser(name="bob", role=MockEnum.Admin)

        is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.CREATE)

        self.assertEqual(is_allowed, True)

    def test_guest_read_dashboard(self):
        rbac = RoleBasedAccess()
        bob = MockUser(name="bob", role=MockEnum.Guest)

        is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.READ)

        self.assertEqual(is_allowed, True)
