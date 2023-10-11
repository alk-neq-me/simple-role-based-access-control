use crate::common::{Authenticator, Permission, Action};

pub struct RoleBasedAccess;

impl<R> Authenticator<R> for RoleBasedAccess
where
    R: ToString
{
    fn is_authenticated<T: Permission>(&self, permission: T, role: R, action: Action) -> bool {
        let mut access = false;
        let mut perms: Vec<&str> = vec![];
        let role = role.to_string();

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

        if perms.contains(&"*") {
            access = true;
        } else if perms.contains(&role.as_str()) {
            access = true;
        }

        access
    }
}
