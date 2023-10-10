from dataclasses import dataclass
from unittest import TestCase

from rbac import RoleBasedAccess, Role, Action
from permissions.dashboard import DashboardPermission


@dataclass(frozen=True)
class MockUser:
    name: str
    role: Role

class TestPermission(TestCase):
    def test_admin_create_dashboard(self):
        rbac = RoleBasedAccess()
        bob = MockUser(name="bob", role=Role.ADMIN)

        is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.CREATE)

        self.assertEqual(is_allowed, True)

    def test_guest_read_dashboard(self):
        rbac = RoleBasedAccess()
        bob = MockUser(name="bob", role=Role.GUEST)

        is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.READ)

        self.assertEqual(is_allowed, True)
