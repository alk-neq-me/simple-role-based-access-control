from abc import ABC, abstractmethod
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import List
from uuid import UUID

from .exception import NotFoundRepo
from .models import Forbidden, Post, RoleEnum, User


class Repository(ABC):
    collection: List

    @abstractmethod
    def fetch_all(
        self,
        # query
    ) -> Callable[[User], None]:
        """Repository fetch_all to implement"""

    @abstractmethod
    def create(
        self, 
        payload
    ) -> Callable[[User], List]:
        """Repository create to implement"""

    @abstractmethod
    def update(
        self, 
        id: UUID, payload
    ) -> Callable[[User], None]:
        """Repository update to implement"""

    """Other CURD implements"""


@dataclass(frozen=False)
class PostRepository(Repository):
    collection: List[Post] = field(default_factory=list, init=False)

    def fetch_all(self) -> Callable[[User], List[Post]]:
        def service(_: User) -> List[Post]:
            return self.collection
        return service

    def create(
        self, 
        payload: Post
    ) -> Callable[[User], None]:
        """Should allow to create post, even which is not admin's posts?"""
        def service(user: User) -> None:
            print(f"New post is created by {user.name}")
            self.collection.append(payload)
        return service

    def update(
        self, 
        id: UUID, 
        payload: Post
    ) -> Callable[[User], None]:
        """Should allow to update post, even which is not admin's posts?"""
        def service(user: User) -> None:
            if not user.role == RoleEnum.ADMIN:
                if not user.id == payload.user.id:
                    raise Forbidden("This is Not your posts")
            for i, p in enumerate(self.collection):
                if p.id == id:
                    self.collection[i] = payload
                    print(f"{payload.user.name} post's is updated by {'admin' if user.role == RoleEnum.ADMIN else user.name}")
                    return
            raise NotFoundRepo(f"Id {id} not found")
        return service
