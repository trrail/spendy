from schemas.users import User


class UserRepository:
    def get_user(self, user_id: str) -> User:
        ...

    def create_user(self) -> User:
        ...

    def update_user(self) -> User:
        ...

    def delete_user(self) -> bool:
        # TODO: Полное удаление пользовательской информации
        ...
