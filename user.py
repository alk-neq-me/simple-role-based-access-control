from rbac.security import AccessRule
from rbac.models import RoleEnum, User, Post
from rbac.repository import PostRepository


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
        role=RoleEnum.EMPLOYEE
    )

    johns_post = Post(
        title="John's first post",
        description="Should own post can delete!",
        user=john
    )

    post_repo = PostRepository()


    bob_db_update = rbac.authorize(
        user=bob, 
        permission="dashboard:update"
    )

    john_db_update = rbac.authorize(
        user=john, 
        permission="dashboard:update"
    )

    print()
    print("Bob", "allowed" if bob_db_update else "denied", "to update dashboard")
    print("John", "allowed" if john_db_update else "denied", "to update dashboard")

    rbac.authorize(
        user=john,
        permission="posts:create",
        callback=post_repo.create(johns_post)
    )

    rbac.authorize(
        # user=rose //-> ❌Error: Not Your post
        # user=bob //-> ✔️  Admin can update, delete
        user=bob, 
        permission="posts:update",  # "posts:delete"  //-> Error: Not Allowed
        callback=post_repo.update(
            id=johns_post.id,
            payload=Post(**{
                **johns_post.__dict__, 
                "description": "updated"
            })
        )
    )


if __name__ == "__main__":
    main()
