import uvicorn

from fastapi import FastAPI
from app.core.database import Base, engine
from app.routes.auth import authrouter
from app.routes.user import userrouter
from app.routes.tweet import tweetrouter
from app.routes.trends import trendsrouter
from app.routes.retweet import retweetrouter
from app.routes.likes import likesrouter
from app.routes.follow import followrouter
from app.routes.comment import commentrouter
from app.routes.message import messagerouter

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
app.include_router(likesrouter.router)
app.include_router(trendsrouter.router)
app.include_router(retweetrouter.router)
app.include_router(followrouter.router)
app.include_router(commentrouter.router)
app.include_router(messagerouter.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)