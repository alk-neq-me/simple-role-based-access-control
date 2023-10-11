use crate::common::Permission;

pub struct DashboardPermission;

impl Permission for DashboardPermission {
    fn create_allowed_roles(&self) -> Vec<&str> {
        vec!["admin", "user"]
    }

    fn read_allowed_roles(&self) -> Vec<&str> {
        vec!["*"]
    }

    fn update_allowed_roles(&self) -> Vec<&str> {
        vec!["admin", "user"]
    }

    fn delete_allowed_roles(&self) -> Vec<&str> {
        vec!["admin"]
    }
}
