pub mod common;
pub mod rbac;
pub mod permissions;

#[cfg(test)]
mod tests {
    use crate::common::{Action, Authenticator};
    use crate::permissions::dashboard::DashboardPermission;
    use crate::rbac::RoleBasedAccess;

    pub enum MockRole {
        Admin,
        Guest
    }

    impl ToString for MockRole {
        fn to_string(&self) -> String {
            match self {
                MockRole::Admin => format!("admin"),
                MockRole::Guest => format!("guest"),
            }
        }
    }

    struct MockUser<'a> {
        #[allow(unused)]
        name: &'a str,
        role: MockRole
    }

    impl<'a> MockUser<'a> {
        fn new(name: &'a str, role: MockRole) -> MockUser {
            MockUser { name, role }
        }
    }

    #[test]
    fn test_admin_dashboard_create() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Admin);

        let is_allowed = rbac.is_authenticated(DashboardPermission, bob.role, Action::Create);
        assert_eq!(is_allowed, true);
    }

    #[test]
    fn test_admin_dashboard_read() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Admin);

        let is_allowed = rbac.is_authenticated(DashboardPermission, bob.role, Action::Read);
        assert_eq!(is_allowed, true);
    }

    #[test]
    fn test_guest_dashboard_create() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Guest);

        let is_allowed = rbac.is_authenticated(DashboardPermission, bob.role, Action::Create);
        assert_eq!(is_allowed, false);
    }

    #[test]
    fn test_guest_dashboard_read() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Guest);

        let is_allowed = rbac.is_authenticated(DashboardPermission, bob.role, Action::Read);
        assert_eq!(is_allowed, true);
    }
}
