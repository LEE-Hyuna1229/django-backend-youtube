from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer

class VideoListSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1

class VideoDetailSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)


    class Meta:
        model = Video
        fields = "__all__"
        # depth = 1