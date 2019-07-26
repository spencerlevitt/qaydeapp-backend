"""Import"""
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import generics
from api.models import User, UserProfile, UserStatistics, Friends, GameRequest, FinishedGame
from api.serializers import UserSerializer, FriendsSerializer, UserStatisticsSerializer, GameRequestSerializer, FinishedGameSerializer
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permisssions(self):
        permission_classes = []
        if self.action == 'create':
            permissions_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class UserStatisticsViewSet(viewsets.ModelViewSet):
    queryset = UserStatistics.objects.all()
    serializer_class = UserStatisticsSerializer

    def get_permisssions(self):
        permission_classes = []
        if self.action == 'create':
            permissions_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class FriendsViewSet(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

    def get_permisssions(self):
        permission_classes = []
        if self.action == 'create':
            permissions_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class GameRequestViewSet(viewsets.ModelViewSet):
    queryset = GameRequest.objects.all()
    serializer_class = GameRequestSerializer

    def get_permisssions(self):
        permission_classes = []
        if self.action == 'create':
            permissions_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class FinishedGameViewset(viewsets.ModelViewSet):
    queryset = FinishedGame.objects.all()
    serializer_class = FinishedGameSerializer

    def get_permisssions(self):
        permission_classes = []
        if self.action == 'create':
            permissions_classes = [IsAdminUser]
        elif self.action == 'retrieve':
            permissions_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
