from schemas.users import User


class UserRepository:
    def get_user(self, nickname: str) -> User:
        ...

    def create_user(self) -> User:
        ...

    def update_user(self) -> User:
        ...

    def delete_user(self) -> bool:
        ...
