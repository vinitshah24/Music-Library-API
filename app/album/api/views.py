from rest_framework import generics
from django.contrib.auth import authenticate, get_user_model
from artist.api.permissions import AnonPermissionOnly, IsOwnerOrReadOnly
from rest_framework import status
from .serializers import AlbumSerializer
from album.models import Album as AlbumModel
from song.models import Song as SongModel
from app.rest.pagination import CustomSingleObjectPagination
from rest_framework import permissions
from django.db.models import Q
from rest_framework.response import Response
import json
from django.core import serializers

Artist = get_user_model()


class AlbumListView(generics.ListAPIView):
    permission_classes = [AnonPermissionOnly]
    serializer_class = AlbumSerializer
    queryset = AlbumModel.objects.all()
    pagination_class = CustomSingleObjectPagination


class AlbumCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [AnonPermissionOnly]
    serializer_class = AlbumSerializer
    queryset = AlbumModel.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user)
            authenticated_username = request.user
            data = request.data
            name = data.get('name')
            song_id = data.get('song_id')
            querySet = Artist.objects \
                .filter(Q(username__iexact=authenticated_username)
                        | Q(email__iexact=authenticated_username)) \
                .distinct()
            if querySet.count() == 1 and data.get('name') is not None \
                    and data.get('song_id') is not None:
                artist = querySet.first()
                print(artist)
                song_id = data.get('song_id')
                song = SongModel.objects.filter(id=song_id)
                json_ser = serializers.serialize('json', song)
                json_data = json.loads(json_ser)
                if json_data[0]['fields']['artist'] == artist.id:
                    print("USER OWNS THE SONG")
                    try:
                        album = AlbumModel.objects.create(
                            name=data.get('name'),
                        )
                    except:
                        return Response(
                            {"message": "Album with same name exists!"},
                            status=status.HTTP_400_BAD_REQUEST
                        )
                    album.song.set(song)
                    return Response(
                        {"message": "Album Created Successfully!"},
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {"message": "Song is not owned by you!"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            elif querySet.count() == 1 and data.get('name') is not None \
                    and data.get('song_id') is None:
                print("No song id provided")
                AlbumModel.objects.create(name=data.get('name'))
                return Response(
                    {"message": "Album Created with No Songs!"},
                    status=status.HTTP_201_CREATED
                )
        return Response(
            {"message": "Error has Occured!"},
            status=status.HTTP_400_BAD_REQUEST
        )


class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AlbumSerializer
    lookup_url_kwarg = 'id'
    queryset = AlbumModel.objects.all()

    # Update partial fields instead of whole object
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response(
            {"message": "Album Deleted Successfully!"},
            status=status.HTTP_200_OK
        )
