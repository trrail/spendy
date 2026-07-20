from repositories.users import UserRepository
from schemas.users import User


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get_user(self, nickname: str) -> User:
        result = self.repository.get_user(nickname)
        return result

    def create_user(self) -> User:
        result = self.repository.create_user()
        return result

    def update_user(self) -> User:
        result = self.repository.update_user()
        return result

    def delete_user(self) -> bool:
        result = self.repository.delete_user()
        return result
