from repositories.users import UserRepository
from services.users import UserService


# repository - работа с БД
user_repository = UserRepository()

# service - работа с бизнес-логикой
user_service = UserService(user_repository)


def get_user_service() -> UserService:
    return user_service
