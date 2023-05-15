from model import AccessRule, RoleEnum, User


rbac = AccessRule()

bob = User(
    name="bob", 
    email="bob@bob", 
    role=RoleEnum.ADMIN
)

john = User(
    name="John",
    email="j@j",
    role=RoleEnum.GUEST
)


bob_db_update = rbac.authorize(
    user=bob, permission="dashboard:update"
)

john_db_update = rbac.authorize(
    user=john, permission="dashboard:update"
)


def main() -> None:
    print()
    print("Bob", "allowed" if bob_db_update else "denied", "to update dashboard")
    print("John", "allowed" if john_db_update else "denied", "to update dashboard")


if __name__ == "__main__":
    main()
