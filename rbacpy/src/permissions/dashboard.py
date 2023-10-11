from dataclasses import dataclass
from typing import List

from common import Permission


@dataclass(frozen=True)
class DashboardPermission(Permission):
    def create_allowed_roles(self) -> List[str]:
        allowed_roles = ["admin", "user"]
        return allowed_roles

    def read_allowed_roles(self) -> List[str]:
        allowed_roles = ["*"]
        return allowed_roles

    def update_allowed_roles(self) -> List[str]:
        allowed_roles = ["admin", "user"]
        return allowed_roles

    def delete_allowed_roles(self) -> List[str]:
        allowed_roles = ["admin"]
        return allowed_roles

