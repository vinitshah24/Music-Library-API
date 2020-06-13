from rest_framework import serializers

from album.models import Album as AlbumModel
from song.api.serializers import SongSerializer


class AlbumSerializer(serializers.ModelSerializer):

    # Nested JSON Obj for Song
    #song = SongSerializer(many=True, read_only=True)

    class Meta:
        model = AlbumModel
        fields = '__all__'
