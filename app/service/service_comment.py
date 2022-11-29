from ..repository.repo_comment import RepoComment
from ..schema.comment import CommentSchema

class ServiceComment(RepoComment):
    def __init__(self, session):
        super().__init__(session)

    def getComments(self, tweetid: int):
        return super().getComments(tweetid)

    def wasCommentBy(self, commentBy: int, commentOn: int):
        return super().wasCommentBy(commentBy, commentOn)

    def createComment(self, tweetid: int, comment: CommentSchema):
        return super().createComment(tweetid, comment)

    def deleteComment(self, commentid: int):
        return super().deleteComment(commentid)