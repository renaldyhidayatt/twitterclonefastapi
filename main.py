import uvicorn

from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes.auth import authrouter

app = FastAPI();


@app.on_event("startup")
async def runtimestartup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(authrouter.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)