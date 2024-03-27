from django.db import models
from common.models import CommonModel

# ChatRoom 모델을  분리했을 때의 이점
# - 관리의 용이
# - 확장성 (채팅방: 오픈채팅방, 업무채팅방,-비밀번호 입력해야 들어 갈 수 있다 등 확장이   용이함)
class ChatRoom(CommonModel):
    name = models.CharField(max_length=100)


class ChatMessage(CommonModel):
    sender = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True) # 알수없음
    message = models.TextField()
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)

# User:Msg(FK) => 1:N
#   - User:Msg,Msg,Msg => o
#   - Msg: User,User,User => X

# Room(부모) - 메세지(자녀)
# Room:Msg(FK) => 1:N
    # - Room: Msg, Msg, Msg => O
    # - Msg: Room, Room, Room => X