from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Observation
from .serializers import ObservationSerializer


class ObservationList(generics.ListCreateAPIView):
    """
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = ObservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ObservationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = ObservationSerializer

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
