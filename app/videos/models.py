from django.db import models
from common.models import CommonModel
from users.models import User

# Create your models here.
class Video(CommonModel):
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveBigIntegerField(default=0)
    thumbnail = models.URLField() # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법

    user = models.ForeignKey(User, on_delete=models.CASCADE) 

# User:Video => 1:N
    # => User : Video, Video, Video, Video, Video => (O)
    # => Video: User, User, User (유튜버 3명이 찍은 영상) => (O)
    #

    # makemigrations (장고한테 알려주는 것)
    # migrate (장고가 DB 찾아가는 것)
    # docker-compose run --rm app sh -c 'python manage.py makemigrations'
