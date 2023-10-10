@dataclass(frozen=True)
class DashboardPermission(Permission):
    def create_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ADMIN, Role.USER]
        return allowed_roles

    def read_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ALL]
        return allowed_roles

    def update_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ADMIN, Role.USER]
        return allowed_roles

    def delete_allowed_roles(self) -> List[Role]:
        allowed_roles = [Role.ADMIN]
        return allowed_roles

