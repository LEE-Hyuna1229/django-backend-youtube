from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubSerializer 
from .models import Subscription
from rest_framework import status
#from rest_framework.exceptions import NotFound
# Create your views here.
# 구독 관련 REST API

# SubscriptionList
# api/v1/subscribtion
# [POST]: 구독하기
class SubscriptionList(APIView):
    def post(self, request):
        user_data = request.data # json -> object  (Serializer 통해 json을 django object로 만듬)
        serializer = SubSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)
        serializer.save(subscriber=request.user)

        return Response(serializer.data, 201)
# SubscriptionDetail
# api/v1/subscription/{user_id}
# [GET]: 특정 유저의 구독자 리스트 조회
# [DELETE]: 구독 취소
class SubscriptionDetail(APIView):
    def get(self,request,pk):
        subs = Subscription.objects.filter(subscribed_to=pk)
        serializer = SubSerializer(subs, many=True)

        return Response(serializer.data)
    
    def delete(self, request,pk):
        
        sub = get_object_or_404(Subscription, pk=pk, subscriber=request.user)
        sub.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

