import uvicorn

from fastapi import FastAPI
from app.core.database import Base, engine
from app.core.config import Settings
from app.routes.main import main_router
from app.core.check_connect import check_db_connected, check_db_disconnected


app = FastAPI(
    title=Settings.PROJECT_NAME,
    version=Settings.PROJECT_VERSION
);


@app.on_event("startup")
async def runtimestartup():
    await check_db_connected()
    Base.metadata.create_all(bind=engine)
    


@app.on_event("shutdown")
async def runtimestop():
    await check_db_disconnected()

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)