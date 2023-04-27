from sqlalchemy.orm import Session
from ..repository.repo_comment import RepoComment
from ..schema.comment import CommentSchema


class ServiceComments():
    def __init__(self, session: Session) -> None:
        self.comment_repository = RepoComment(session)


    def get_comments(self, tweetid: int):
        try:
            comment = self.comment_repository.getComments(tweetid=tweetid)

            if not comment:
                raise Exception("Not found Comment:")

            return comment
        except Exception as e:
            raise Exception("Something went wrong : {}".format(e))

    def was_commentby(self, commentBy: int, commentOn: int):
        try:
            comment = self.comment_repository.wasCommentBy(commentBy=commentBy, commentOn=commentOn)

            if not comment:
                raise Exception("Comment not found for user with ID {} on post with ID {}".format(commentBy, commentOn))
            
            return comment
        except Exception as e:
            raise Exception("Something wenat wrong: {}".format(e))

    def createComment(self, tweetid: int, comment: CommentSchema):
        return self.comment_repository.createComment(tweetid, comment)

    def deleteComment(self, commentid: int):
        return self.comment_repository.deleteComment(commentid)
