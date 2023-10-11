pub mod common;
pub mod rbac;

#[cfg(test)]
mod tests {
    use crate::common::{Action, Authenticator, Permission};
    use crate::rbac::RoleBasedAccess;

    struct DashboardPermission;

    impl Permission for DashboardPermission {
        type Role = MockRole;

        fn create_allowed_roles(&self) -> Vec<Self::Role> {
            vec![MockRole::Admin]
        }

        fn read_allowed_roles(&self) -> Vec<Self::Role> {
            vec![MockRole::Admin, MockRole::User, MockRole::Guest]
        }

        fn update_allowed_roles(&self) -> Vec<Self::Role> {
            vec![MockRole::Admin, MockRole::User]
        }

        fn delete_allowed_roles(&self) -> Vec<Self::Role> {
            vec![MockRole::Admin]
        }
    }

    #[derive(PartialEq)]
    enum MockRole {
        Admin,
        User,
        Guest,
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

        let is_allowed = rbac.is_authenticated(&DashboardPermission, &bob.role, &Action::Create);
        assert_eq!(is_allowed, true);
    }

    #[test]
    fn test_admin_dashboard_read() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Admin);

        let is_allowed = rbac.is_authenticated(&DashboardPermission, &bob.role, &Action::Read);
        assert_eq!(is_allowed, true);
    }

    #[test]
    fn test_guest_dashboard_create() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Guest);

        let is_allowed = rbac.is_authenticated(&DashboardPermission, &bob.role, &Action::Create);
        assert_eq!(is_allowed, false);
    }

    #[test]
    fn test_guest_dashboard_read() {
        let rbac = RoleBasedAccess;
        let bob = MockUser::new("Bob", MockRole::Guest);

        let is_allowed = rbac.is_authenticated(&DashboardPermission, &bob.role, &Action::Read);
        assert_eq!(is_allowed, true);
    }
}
