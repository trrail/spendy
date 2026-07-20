from fastapi import routing, Depends

from app.core.depends import get_user_service
from app.schemas.users import User
from app.services.users import UserService
from starlette import status

router = routing.APIRouter(tags=["Users"], prefix="/users")


@router.get(
    '/{user_id}/',
    response_model=User,
    description='Получение пользователя'
)
async def get_users(user_id: str, user_service: UserService = Depends(get_user_service)) -> User:
    user = user_service.get_user(user_id)
    return user

@router.post(
    '/',
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    description='Создание пользователя'
)
async def create_user(user_service: UserService = Depends(get_user_service)) -> User:
    user = user_service.create_user()
    return user

@router.put(
    '/{user_id}/',
    response_model=User,
    description='Обновление информации о пользователе'
)
async def update_user(user_id: int, user_service: UserService = Depends(get_user_service)) -> User:
    user = user_service.update_user()
    return user

@router.delete(
    '/{user_id}/',
    status_code=status.HTTP_204_NO_CONTENT,
    description='Удаление пользователя'
)
async def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)) -> None:
    user_service.delete_user()
    return None
