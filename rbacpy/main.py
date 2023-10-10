from __future__ import annotations

from dataclasses import dataclass
import logging


@dataclass(frozen=True)
class User:
    name: str
    role: Role


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
