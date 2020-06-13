from rest_framework import generics
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework.response import Response
from song.models import Song as SongModel
from rest_framework import status

from .serializers import SongSerializer

from artist.api.permissions import AnonPermissionOnly, IsOwnerOrReadOnly
from rest_framework import permissions
from app.rest.pagination import CustomPagination

Artist = get_user_model()


class SongListView(generics.ListAPIView):
    permission_classes = [AnonPermissionOnly]
    serializer_class = SongSerializer
    queryset = SongModel.objects.all()
    pagination_class = CustomPagination


class SongCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SongSerializer
    queryset = SongModel.objects.all()

    def create(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user)
            authenticated_username = request.user
            data = request.data
            name = data.get('name')
            year_released = data.get('year_released')
            genre = data.get('genre')
            querySet = Artist.objects \
                .filter(Q(username__iexact=authenticated_username)
                        | Q(email__iexact=authenticated_username)) \
                .distinct()
            if querySet.count() == 1 and data.get('name') is not None \
                    and data.get('year_released') is not None \
                    and data.get('genre') is not None:
                artist = querySet.first()
                try:
                    song = SongModel.objects.create(
                        name=data.get('name'),
                        year_released=data.get('year_released'),
                        genre=data.get('genre'),
                        artist=artist
                    )
                    song.save()
                    return Response(
                        {"message": "Song Created Successfully!"},
                        status=status.HTTP_201_CREATED
                    )
                except:
                    return Response(
                        {"message": "Song Name Already Exist!"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(
            {"message": "Error has Occured!"},
            status=status.HTTP_400_BAD_REQUEST
        )


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SongSerializer
    lookup_url_kwarg = 'id'
    queryset = SongModel.objects.all()

    # Update partial fields instead of whole object
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    # Reference: http://www.cdrf.co/2.2/rest_framework.generics/DestroyAPIView.html
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response(
            {"message": "Song Deleted Successfully!"},
            status=status.HTTP_200_OK
        )
