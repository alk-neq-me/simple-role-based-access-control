# Simple Role-Based Access Control (RBAC) System
[![Rust Test](https://github.com/alk-neq-me/simple-role-based-access-control/actions/workflows/rust_test.yml/badge.svg)](https://github.com/alk-neq-me/simple-role-based-access-control/actions/workflows/rust_test.yml)
[![Python Test](https://github.com/alk-neq-me/simple-role-based-access-control/actions/workflows/python_test.yml/badge.svg)](https://github.com/alk-neq-me/simple-role-based-access-control/actions/workflows/python_test.yml)
[![License](https://img.shields.io/github/license/alk-neq-me/simple-role-based-access-control)](https://github.com/alk-neq-me/simple-role-based-access-control/blob/main/LICENSE)

This project is a simple implementation of a Role-Based Access Control (RBAC) system in Python and Rust.

## Python Version

### Description

The Python version of this RBAC system uses data classes and predefined permissions to manage access control. It offers a structured approach to implementing RBAC, making it reusable, maintainable, and clean.

### Usage

To use the Python version, follow these steps:

1. Install the RBAC package from this GitHub repository:

   ```bash
   git clone https://github.com/alk-neq-me/simple-role-based-access-control.git
   ```

2. Use the RBAC system in your code:

   ```python
   from dataclasses import dataclass
   from rbac import RoleBasedAccess, Role, Action
   from permissions.dashboard import DashboardPermission
   from enum import Enum

   class Role(str, Enum):
       Admin = "admin"
       User = "user"
       Guest = "guest"
       All = "*"

   class DashboardPermission(Permission):
        def create_allowed_roles(self) -> List[Enum]:
            return [Enum.Admin, Enum.User]

        def read_allowed_roles(self) -> List[Enum]:
            return [Enum.All]

        def update_allowed_roles(self) -> List[Enum]:
            return [Enum.Admin, Enum.User]

        def delete_allowed_roles(self) -> List[Enum]:
            return [Enum.Admin]

   @dataclass(frozen=True)
   class MockUser:
       name: str
       role: Role

   # Example usage:
   rbac = RoleBasedAccess[Role]()  #  type safe
   bob = MockUser(name="bob", role=Role.ADMIN)

   # type-safe role: Role, Permission[Role]
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
    }
   ```

3. Replace `rbac::permissions::dashboard::DashboardPermission` with your custom permissions as needed.

