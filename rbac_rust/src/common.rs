pub trait Authenticator<R: ToString> {
    fn is_authenticated<T: Permission>(&self, permission: T, role: R, action: Action) -> bool;
}


pub trait Permission {
    fn create_allowed_roles(&self) -> Vec<&str>;

    fn read_allowed_roles(&self) -> Vec<&str>;

    fn update_allowed_roles(&self) -> Vec<&str>;

    fn delete_allowed_roles(&self) -> Vec<&str>;
}


// #[derive(PartialEq)]
// pub enum Role {
//     Admin,
//     User,
//     Guest,
//     All
// }


#[derive(PartialEq)]
pub enum Action {
    Create,
    Read,
    Update,
    Delete
}
