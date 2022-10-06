from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from community_api.permissions import IsOwnerOrReadOnly
from .models import Observation
from .serializers import ObservationSerializer


class ObservationList(generics.ListCreateAPIView):
    """
    The perform_create method associates the observation
    with the logged in user.
    """
    serializer_class = ObservationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Observation.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'likes__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ObservationDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a observation and edit or delete it if you own it.
    """
    serializer_class = ObservationSerializer

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Observation.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
