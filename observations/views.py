from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Observation
from .serializers import ObservationSerializer
from community_api.permissions import IsOwnerOrReadOnly


class ObservationList(APIView):
    serializer_class = ObservationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        observations = Observation.objects.all()
        serializer = ObservationSerializer(
            observation, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = ObservationSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class ObservationDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ObservationSerializer

    def get_object(self, pk):
        try:
            observation = Observation.objects.get(pk=pk)
            self.check_object_permissions(self.request, observation)
            return observation
        except Observation.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        observation = self.get_object(pk)
        serializer = ObservationSerializer(
            observation, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        observation = self.get_object(pk)
        serializer = ObservationSerializer(
            observation, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        observation = self.get_object(pk)
        observation.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
