import uvicorn
from fastapi import FastAPI
from app.routing.users import router as user_router
from app.core.config import settings


app = FastAPI(title=settings.title, debug=settings.debug)
app.include_router(user_router)

if __name__ == '__main__':
    ...
    # TODO: Не запускается с параметром reload
    # uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)
