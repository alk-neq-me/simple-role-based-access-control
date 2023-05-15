from model import AccessRule, Post, RoleEnum, User


def main() -> None:
    rbac = AccessRule()

    bob = User(
        name="bob", 
        email="bob@bob", 
        role=RoleEnum.ADMIN
    )

    john = User(
        name="John",
        email="j@j",
        role=RoleEnum.GUEST
    )

    rose = User(
        name="Rose",
        email="j@j",
        role=RoleEnum.GUEST
    )

    johns_post = Post(
        title="John's first post",
        description="Should own post can delete!",
        user=john
    )


    bob_db_update = rbac.authorize(
        user=bob, permission="dashboard:update"
    )

    john_db_update = rbac.authorize(
        user=john, permission="dashboard:update"
    )


    print()
    print("Bob", "allowed" if bob_db_update else "denied", "to update dashboard")
    print("John", "allowed" if john_db_update else "denied", "to update dashboard")

    rbac.authorize(
        # user=rose //-> ❌Error: Not Your post
        # user=bob //-> ✔️
        user=bob, 
        permission="posts:update",  # "posts:delete"  //-> Error: Not Allowed
        callback=johns_post.update
    )


if __name__ == "__main__":
    main()
