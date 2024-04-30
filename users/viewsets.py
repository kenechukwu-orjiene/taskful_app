from django.contrib.auth.models import User

from rest_framework import viewsets, mixins

from users.serializers import UserSerializer, ProfileSerializer
from users.models import Profile
from users.permissions import IsUserOwnerOrGetAndPostOnly, IsProfileOwnerOrGetAndPostOnly

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                    #  mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin
                     ):
    permission_classes = [IsProfileOwnerOrGetAndPostOnly, ]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer