from rest_framework import serializers

from song.models import Song as SongModel
from artist.api.serializers import ArtistDetailSerializer


class SongSerializer(serializers.ModelSerializer):

    # Nested JSON Obj for Song Owner
    artist = ArtistDetailSerializer(read_only=True)

    class Meta:
        model = SongModel
        fields = '__all__'
