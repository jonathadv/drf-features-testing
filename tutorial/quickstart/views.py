from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserViewSet(viewsets.ModelViewSet):
    """
    # UserViewSet
    API endpoint that allows users to be viewed or edited.

    ```python
    permission_classes = [IsAuthenticated | ReadOnly]
    ```
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated | ReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]