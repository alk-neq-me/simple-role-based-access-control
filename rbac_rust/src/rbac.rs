use crate::common::{Authenticator, Permission, Action};

pub struct RoleBasedAccess;

impl Authenticator for RoleBasedAccess {
    fn is_authenticated<T: Permission>(&self, permission: &T, role: &T::Role, action: &Action) -> bool {
        let mut access = false;
        let mut perms: Vec<T::Role> = vec![];

        match action {
            Action::Create => {
                perms.extend(permission.create_allowed_roles());
            },
            Action::Read => {
                perms.extend(permission.read_allowed_roles());
            },
            Action::Update => {
                perms.extend(permission.update_allowed_roles());
            },
            Action::Delete => {
                perms.extend(permission.delete_allowed_roles());
            },
        }

        if perms.contains(&role) {
            access = true;
        }

        access
    }
}
