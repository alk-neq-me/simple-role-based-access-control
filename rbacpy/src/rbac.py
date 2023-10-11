import logging
from dataclasses import dataclass
from typing import List

from common import Action, Authoritor, Permission


@dataclass(frozen=True)
class RoleBasedAccess(Authoritor):
    def is_authorized(self, permission: Permission, role: str, action: Action) -> bool:
        access = False
        perm: List[str] = []

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

        if "*" in perm:
            access = True
        elif role in perm:
            access = True

        return access

