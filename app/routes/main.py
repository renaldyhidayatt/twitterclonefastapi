from fastapi import APIRouter
from .auth import authrouter
from .user import userrouter
from .tweet import tweetrouter
from .likes import likesrouter
from .trends import trendsrouter
from .retweet import retweetrouter
from .follow import followrouter
from .comment import commentrouter
from .message import messagerouter

main_router = APIRouter()


main_router.include_router(authrouter.router)
main_router.include_router(userrouter.router)
main_router.include_router(tweetrouter.router)
main_router.include_router(likesrouter.router)
main_router.include_router(trendsrouter.router)
main_router.include_router(retweetrouter.router)
main_router.include_router(followrouter.router)
main_router.include_router(commentrouter.router)
main_router.include_router(messagerouter.router)