CREATE TABLE `comment` (
  `id` tinyint(4) DEFAULT NULL,
  `commentBy_id` tinyint(4) DEFAULT NULL,
  `commentOn_id` tinyint(4) DEFAULT NULL,
  `comment` varchar(17) DEFAULT NULL,
  `commentAt` varchar(0) DEFAULT NULL,
  CONSTRAINT fk_user
    FOREIGN KEY (commentBy_id) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
  CONSTRAINT fk_tweet
    FOREIGN KEY (commentOn_id) 
        REFERENCES tweet(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE `follow` (
  `id` tinyint(4) DEFAULT NULL,
  `sender` tinyint(4) DEFAULT NULL,
  `receiver` tinyint(4) DEFAULT NULL,
  `followOn` varchar(0) DEFAULT NULL,
  CONSTRAINT fk_sender
    FOREIGN KEY (sender) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
  CONSTRAINT fk_receiver
    FOREIGN KEY (receiver) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE `likes` (
  `id` tinyint(4) DEFAULT NULL,
  `likeOn` tinyint(4) DEFAULT NULL,
  `likeBy` tinyint(4) DEFAULT NULL,
  CONSTRAINT fk_likeon
    FOREIGN KEY (likeOn) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
  CONSTRAINT fk_likeby
    FOREIGN KEY (likeBy) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE `messages` (
  `id` tinyint(4) DEFAULT NULL,
  `message` varchar(17) DEFAULT NULL,
  `messageTo` tinyint(4) DEFAULT NULL,
  `messageFrom` tinyint(4) DEFAULT NULL,
  `messageOn` varchar(0) DEFAULT NULL,
  CONSTRAINT fk_messageto
    FOREIGN KEY (messageTo) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
  CONSTRAINT fk_messagefrom
    FOREIGN KEY (messageFrom) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE `retweet` (
  `id` tinyint(4) DEFAULT NULL,
  `retweetBy_id` tinyint(4) DEFAULT NULL,
  `retweetFrom_id` tinyint(4) DEFAULT NULL,
  `status` varchar(4) DEFAULT NULL,
  `tweetOn` varchar(0) DEFAULT NULL,
  CONSTRAINT fk_retweetby
    FOREIGN KEY (retweetBy_id) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
  CONSTRAINT fk_retweetfrom
    FOREIGN KEY (retweetFrom_id) 
        REFERENCES tweet(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE `trend` (
  `id` tinyint(4) DEFAULT NULL,
  `hashtag` varchar(5) DEFAULT NULL,
  `user_id` tinyint(4) DEFAULT NULL,
  `tweet_id` tinyint(4) DEFAULT NULL,
  CONSTRAINT fk_user
    FOREIGN KEY (user_id) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
  CONSTRAINT fk_tweet
    FOREIGN KEY (tweet_id) 
        REFERENCES tweet(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

CREATE TABLE `tweet` (
  `id` tinyint(4) DEFAULT NULL,
  `status` varchar(15) DEFAULT NULL,
  `tweetBy_id` tinyint(4) DEFAULT NULL,
  `postedOn` varchar(0) DEFAULT NULL,
  CONSTRAINT fk_tweetby
    FOREIGN KEY (tweetBy_id) 
        REFERENCES user(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
);

CREATE TABLE `user` (
  `id` tinyint(4) DEFAULT NULL,
  `firstName` varchar(5) DEFAULT NULL,
  `lastName` varchar(3) DEFAULT NULL,
  `username` varchar(8) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `password` varchar(60) DEFAULT NULL,
  `profileImage` varchar(21) DEFAULT NULL,
  `profileCover` varchar(22) DEFAULT NULL,
  `bio` varchar(0) DEFAULT NULL,
  `country` varchar(0) DEFAULT NULL,
  `website` varchar(0) DEFAULT NULL
);
