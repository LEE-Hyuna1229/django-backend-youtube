from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q
# from user.models import User
# from viedos.models import Video

# - User: FK
# - Video: Fk
# - reaction (like,dislike,cancel)

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'likes'),
        (DISLIKE, 'dislikes'),
        (NO_REACTION, 'No Reaction')
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default = NO_REACTION
    )

    
    @staticmethod # ORM depth2 모델.obects.get, filter().aggregate() #SQL: JOIN QUERY
    def get_video_reaction(video): # 1번 비디오 - 좋아요/싫어요 갯수 궁금
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )

        return reactions