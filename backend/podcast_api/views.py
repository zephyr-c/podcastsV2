from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from .serializers import PodcastSerializer
from .models import Podcast

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all().order_by('date_added')
    serializer_class = PodcastSerializer



    @action(detail=True, methods=['post', 'put'])
    def like(self, request, pk=None):
        podcast = self.get_object()
        podcast.like()
        podcast.save()
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post', 'put'])
    def dislike(self, request, pk=None):
        podcast = self.get_object()
        podcast.dislike()
        podcast.save()
        return Response(status=status.HTTP_200_OK)
