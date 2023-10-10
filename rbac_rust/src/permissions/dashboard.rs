use crate::common::{Permission, Role};

pub struct DashboardPermission;

impl Permission for DashboardPermission {
    fn create_allowed_roles(&self) -> Vec<Role> {
        vec![Role::Admin, Role::User]
    }

    fn read_allowed_roles(&self) -> Vec<Role> {
        vec![Role::All]
    }

    fn update_allowed_roles(&self) -> Vec<Role> {
        vec![Role::Admin, Role::User]
    }

    fn delete_allowed_roles(&self) -> Vec<Role> {
        vec![Role::Admin]
    }
}
