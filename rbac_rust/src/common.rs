pub trait Authenticator {
    fn is_authenticated<T: Permission>(&self, permission: T, role: Role, action: Action) -> bool;
}


pub trait Permission {
    fn create_allowed_roles(&self) -> Vec<Role> {
        vec![]
    }

    fn read_allowed_roles(&self) -> Vec<Role> {
        vec![]
    }

    fn update_allowed_roles(&self) -> Vec<Role> {
        vec![]
    }

    fn delete_allowed_roles(&self) -> Vec<Role> {
        vec![]
    }
}


#[derive(PartialEq)]
pub enum Role {
    Admin,
    User,
    Guest,
    All
}


#[derive(PartialEq)]
pub enum Action {
    Create,
    Read,
    Update,
    Delete
}
