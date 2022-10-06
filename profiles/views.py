from django.db.models import Count
from rest_framework import generics, filters
from community_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.annotate(
        observations_count=Count('owner__observation', distinct=True))

    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'observations_count'
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Profile.objects.annotate(
        observations_count=Count('owner__observation', distinct=True))

    serializer_class = ProfileSerializer
