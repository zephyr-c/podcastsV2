from rest_framework import serializers

from .models import Podcast


class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Podcast
        fields = (
            'id',
            'name',
            'description',
            'source',
            'audio',
            'image',
            'episode_title',
            'numLikes',
            'numDislikes',
            'date_added',
        )
