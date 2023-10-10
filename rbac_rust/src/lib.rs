pub mod common;
pub mod rbac;
pub mod permissions;

#[cfg(test)]
mod tests {
    use crate::common::{Role, Action, Authenticator};
    use crate::permissions::dashboard::DashboardPermission;
    use crate::rbac::RoleBasedAccess;

    struct MockUser<'a> {
        #[allow(unused)]
        name: &'a str,
        role: Role
    }

    impl<'a> MockUser<'a> {
        fn new(name: &'a str, role: Role) -> MockUser {
            MockUser { name, role }
        }
    }

    #[test]
    fn it_works() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", Role::Guest);

        let is_allowed = rbac.is_authenticated(DashboardPermission, bob.role, Action::Read);

        assert_eq!(is_allowed, true);
    }
}
