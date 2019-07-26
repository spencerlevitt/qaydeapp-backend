"""Imports"""
from django.urls import path, include
from rest_framework import routers
from api.views import UserViewSet, FriendsViewSet, GameRequestViewSet, FinishedGameViewset, UserStatisticsViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('userstats', UserStatisticsViewSet)
router.register('friends', FriendsViewSet)
router.register('gamerequests', GameRequestViewSet)
router.register('finishedgames', FinishedGameViewset)

urlpatterns = [

    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),

]
