import uvicorn
from fastapi import FastAPI
from routing.users import router as user_router

app = FastAPI(debug=True)
app.include_router(user_router)

if __name__ == '__main__':
    ...
    # TODO: Не запускается с параметром reload
    # uvicorn.run(app, host='127.0.0.1', port=8000, reload=True)
