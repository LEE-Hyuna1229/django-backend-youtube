from django.db import models
from common.models import CommonModel
from users.models import User
from videos.models import Video

class Comment(CommonModel):
    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)

    # User: Comment
    # - User => Comment, Comment, Comment, Comment (O)
    # - Comment => User, User, User (X) 

    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Video ;Comment
# - Video => Comment, Comment, Comment 댓글 여러개 가능
# - Comment => Video(침착맨), Video(이지금), Video(빵투버_뽀니) => (X)

    video = models.ForeignKey(Video, on_delete=models.CASCADE)

# docker-compose run --rm app sh -c 'python manage.py makemigrations'
