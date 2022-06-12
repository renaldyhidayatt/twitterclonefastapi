from app.core.database import engine
from sqlalchemy.orm import Session
from app.database.models.Users import User
from app.database.models.Tweet import Tweet
from app.database.models.Likes import Likes
from app.database.models.Comment import Comment
from app.database.models.Follow import Follow
from app.database.models.Messages import Messages
from app.database.models.Retweet import Retweet

def createuser():
    session = Session(engine)
    user = User(
        firstName="John",
        lastName="Doe",
        username="johndoe",
        email="last@example.com",
        password="johndoe",
    )
    session.add(user)
    session.commit()
    session.close()

def createuser2():
    session = Session(engine)
    user = User(
        firstName="John2",
        lastName="Doe",
        username="johndoe2",
        email="johndoe2@example.com",
        password="johndoe",
    )
    session.add(user)
    session.commit()
    session.close()

def createTweet():
    session = Session(engine)
    tweet = Tweet(
        tweetBy=1,
        status="This is a tweet"
    )
    session.add(tweet)
    session.commit()
    session.close()


def createLikes():
    session = Session(engine)
    likes = Likes(
        likeBy=1,
        likeOn=1
    )
    session.add(likes)
    session.commit()
    session.close()


def createComment():
    session = Session(engine)
    comment = Comment(
        commentBy=1,
        commentOn=1,
        comment="This is a comment"
    )
    session.add(comment)
    session.commit()
    session.close()

def createFollow():
    session = Session(engine)
    follow = Follow(
        sender=1,
        receiver=1
    )
    session.add(follow)
    session.commit()
    session.close()


def createMessages():
    session = Session(engine)
    messages = Messages(
        messageTo=1,
        messageFrom=2,
        message="This is a message"
    )
    session.add(messages)
    session.commit()
    session.close()

def createRetweet():
    session = Session(engine)
    retweet = Retweet(
        retweetBy=1,
        retweetFrom=1,
        status="This is a retweet"
    )
    session.add(retweet)
    session.commit()
    session.close()

if __name__ == "__main__":
    createuser()
    createuser2()
    createTweet()
    createLikes()
    createComment()
    createFollow()
    createMessages()
    createRetweet()
    print("Database seeded")