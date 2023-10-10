from __future__ import annotations

from dataclasses import dataclass
import logging

from common import Action, Role
from permissions.dashboard import DashboardPermission
from rbac import Rbac




def main():
    logging.basicConfig(
        format="[  ] %(message)s", 
        datefmt="%Y-%m-%d",
        level=logging.WARN
    )
    rbac = Rbac()

    user = User()

    is_allowed = rbac.is_authorized(
        permission=DashboardPermission(), 
        role=user.role, 
        action=Action.UPDATE
    )

    print(is_allowed)


if __name__ == "__main__":
    main()
