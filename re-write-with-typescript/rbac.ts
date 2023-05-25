type ActionEnum =
  | "read"
  | "create"
  | "update"
  | "delete"
  | "*"
  | "!"


type RoleEnum =
  | "admin"
  | "guest"
  | "user"
  | "employee"
  | "manager"


type User = {
  name: string,
  role: RoleEnum
}


class Permission {
  resource: string;
  action: ActionEnum;

  constructor(resource: string, action: ActionEnum) {
    this.resource = resource;
    this.action = action;
  }

  get name() {
    return `${this.resource}:${this.action}`
  }
}


type Role = {
  name: RoleEnum,
  permissions: Permission[]
}


function log_perms(rules: Map<RoleEnum, Role>, role: RoleEnum) {
  const current_rule = rules.get(role);

  if (!current_rule) throw new Error("Not Found Role name");

  for (const perm of current_rule?.permissions) {
    console.log("[ Permission ]", perm);
  }
}


class AccessRule {
  access_rules: Map<RoleEnum, Role> = new Map([
    ["admin", {
      name: "admin", 
      permissions: [
        new Permission("*", "*")
      ]
    }],

    ["guest", { 
      name: "guest", 
      permissions: [
        new Permission("post", "read"),
      ]
    }]
  ]);

  authorize<U extends { role: RoleEnum }>(user: U, permission: string) {
    let access: boolean = false;
    const [resource, action] = permission.split(":");

    log_perms(this.access_rules, user.role);
  
    for (const access_rule of this.access_rules.values()) {
      if (access_rule.name === user.role) {
        for (const permission of access_rule.permissions) {
          if (
            (resource == permission.resource || permission.resource === "*") 
              && (permission.action === action || permission.action === "*")
          ) {
            access = true
          }
          if (resource == permission.resource && permission.action === "!") {
            access = false
          }
        }
      }
    }

    return access;
  }
}


function main() {
  const admin: User = {
    name: "bob",
    role: "admin"
  }

  const anonymous: User = {
    name: "some",
    role: "guest"
  }

  const rbac = new AccessRule();

  const admin_dashboard_edit_perm = rbac.authorize(admin, "dashboard:edit");

  const guest_post_read_perm = rbac.authorize(anonymous, "post:read");
  const guest_dashboard_edit_perm = rbac.authorize(anonymous, "dashboard:edit");

  console.log({ admin_dashboard_edit_perm });
  console.log({ guest_post_read_perm });
  console.log({ guest_dashboard_edit_perm });
}


main()
