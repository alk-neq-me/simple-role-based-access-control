pub trait Authenticator {
    fn is_authenticated<T: Permission>(&self, permission: &T, role: &T::Role, action: &Action) -> bool;
}


pub trait Permission {
    type Role: PartialEq;
    fn create_allowed_roles(&self) -> Vec<Self::Role> {
        vec![]
    }

    fn read_allowed_roles(&self) -> Vec<Self::Role> {
        vec![]
    }

    fn update_allowed_roles(&self) -> Vec<Self::Role> {
        vec![]
    }

    fn delete_allowed_roles(&self) -> Vec<Self::Role> {
        vec![]
    }
}


#[derive(PartialEq)]
pub enum Action {
    Create,
    Read,
    Update,
    Delete
}
