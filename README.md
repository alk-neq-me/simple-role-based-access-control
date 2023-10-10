# Simple Role-Based Access Control (RBAC) System

This project is a simple implementation of a Role-Based Access Control (RBAC) system in Python and Rust.

## Python Version

### Description

The Python version of this RBAC system uses data classes and predefined permissions to manage access control. It offers a structured approach to implementing RBAC, making it reusable, maintainable, and clean.

### Usage

To use the Python version, follow these steps:

1. Install the RBAC package from this GitHub repository:

   ```bash
   pip install git+https://github.com/alk-neq-me/simple-role-based-access-control.git
   ```

2. Use the RBAC system in your code:

   ```python
   from dataclasses import dataclass
   from rbac import RoleBasedAccess, Role, Action
   from permissions.dashboard import DashboardPermission

   @dataclass(frozen=True)
   class MockUser:
       name: str
       role: Role

   # Example usage:
   rbac = RoleBasedAccess()
   bob = MockUser(name="bob", role=Role.ADMIN)

   is_allowed = rbac.is_authorized(permission=DashboardPermission(), role=bob.role, action=Action.CREATE)

   assert is_allowed == True
   ```

3. Replace `permissions.dashboard.DashboardPermission` with your custom permissions as needed.

## Rust Version

### Description

The Rust version of this RBAC system uses Rust's strong type system and enums to implement access control. It provides similar RBAC functionality to the Python version.

### Usage

To use the Rust version, follow these steps:

1. Add the RBAC crate as a dependency in your `Cargo.toml` file:

   ```toml
   [dependencies]
   rbac = { git = "https://github.com/alk-neq-me/simple-role-based-access-control" }
   ```

2. Use the RBAC system in your code:

   ```rust
   #[cfg(test)]
   mod tests {
       use rbac::common::{Role, Action, Authenticator};
       use rbac::permissions::dashboard::DashboardPermission;
       use rbac::rbac::RoleBasedAccess;

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
   ```

3. Replace `rbac::permissions::dashboard::DashboardPermission` with your custom permissions as needed.

