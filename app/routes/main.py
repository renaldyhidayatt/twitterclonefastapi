from fastapi import APIRouter
from . import authrouter, userrouter, tweetrouter, trendsrouter, retweetrouter, messagerouter, likesrouter, followrouter
from .comment import commentrouter

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