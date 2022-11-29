from app.core.database import engine
from sqlalchemy.orm import Session
from app.database.models.Users import User
from app.database.models.Tweet import Tweet
from app.database.models.Likes import Likes
from app.database.models.Trends import Trends
from app.database.models.Comment import Comment
from app.database.models.Follow import Follow
from app.database.models.Messages import Messages
from app.database.models.Retweet import Retweet
from app.core.hashpassword import HashPassword

class SeedConfig:
    def __init__(self, session):
        self.session = session
    
    def createuser(self):
        user = User(
            firstName="John",
            lastName="Doe",
            username="johndoe",
            email="last@example.com",
            password=HashPassword.create_hash("johndoe"),
        )
        self.session.add(user)
        self.session.commit()
        return user

    def createuser2(self):
        user = User(
            firstName="John2",
            lastName="Doe",
            username="johndoe2",
            email="johndoe2@example.com",
            password=HashPassword.create_hash("johndoe2"),
        )
        self.session.add(user)
        self.session.commit()

        return user

    def createTweet(self):
        tweet = Tweet(
            tweetBy_id=1,
            status="This is a tweet"
        )
        self.session.add(tweet)
        self.session.commit()


    def createLikes(self):
        likes = Likes(
            likeBy=1,
            likeOn=1
        )
        self.session.add(likes)
        self.session.commit()

    def createTrend(self):
        trend = Trends(
            user_id=1,
            tweet_id=1,
            hashtag="dota2"
        )
        self.session.add(trend)
        self.session.commit()
        return trend

    def createComment(self):
        comment = Comment(
            commentBy_id=1,
            commentOn_id=1,
            comment="This is a comment"
        )
        self.session.add(comment)
        self.session.commit()

    def createFollow(self):
        follow = Follow(
            sender=1,
            receiver=1
        )
        self.session.add(follow)
        self.session.commit()

    def createMessages(self):
        messages = Messages(
            messageTo=1,
            messageFrom=2,
            message="This is a message"
        )
        self.session.add(messages)
        self.session.commit()
    def createRetweet(self):
        retweet = Retweet(
            retweetBy_id=1,
            retweetFrom_id=1,
            status="This is a retweet"
        )
        self.session.add(retweet)
        self.session.commit()





SessionConfig = Session(engine)

Seed = SeedConfig(SessionConfig)






if __name__ == "__main__":
    Seed.createuser()
    Seed.createuser2()
    Seed.createTweet()
    Seed.createLikes()
    Seed.createComment()
    Seed.createFollow()
    Seed.createMessages()
    Seed.createRetweet()
    Seed.createTrend()
    print("Database seeded")