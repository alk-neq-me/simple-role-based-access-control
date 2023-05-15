from model import AccessRule, RoleEnum, User


rbac = AccessRule()

bob = User(
    name="bob", 
    email="bob@bob", 
    role=RoleEnum.GUEST
)


authorized = rbac.authorize(
    user=bob, permission="dashboard:read"
)

if authorized:
    print("Access")
else:
    print("Denied")
