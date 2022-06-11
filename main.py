import uvicorn

from fastapi import FastAPI
from app.config.database import Base, engine
from app.routes.auth import authrouter
from app.routes.user import userrouter
from app.routes.tweet import tweetrouter
from app.routes.trends import trendsrouter

app = FastAPI();


@app.on_event("startup")
async def runtimestartup():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(authrouter.router)
app.include_router(userrouter.router)
app.include_router(tweetrouter.router)
app.include_router(trendsrouter.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)