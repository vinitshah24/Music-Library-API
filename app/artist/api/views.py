
import json

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, get_user_model
from django.db.models import Q
from rest_framework import status

from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from .serializers import ArtistSerializer, ArtistAdminSerializer, ArtistDetailSerializer, ArtistListSerializer
from rest_framework.mixins import UpdateModelMixin

# Permissions
from .permissions import AnonPermissionOnly, IsOwnerOrReadOnly, IsAdminUser
from rest_framework import authentication, permissions

Artist = get_user_model()


class ArtistsListView(generics.ListAPIView):

    permission_classes = [AnonPermissionOnly]
    serializer_class = ArtistListSerializer
    passed_id = None
    # Filter
    search_fields = ('username', 'born_date', 'origin', 'genre')
    ordering_fields = ('username', 'born_date', 'origin', 'genre')
    queryset = Artist.objects.all()

    # Returns a dict containing any extra context that should be supplied to serializer
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class LoginView(APIView):
    permission_classes = [AnonPermissionOnly]

    def post(self, request, *args, **kwargs):
        # print(request.user)
        if request.user.is_authenticated:
            return Response({'detail': 'Already authenticated!'}, status=400)
        data = request.data
        email = data.get('email')
        password = data.get('password')
        qs = Artist.objects.filter(Q(email__iexact=email)).distinct()
        if qs.count() == 1:
            artist_obj = qs.first()
            if artist_obj.check_password(password):
                artist = artist_obj
                payload = api_settings.JWT_PAYLOAD_HANDLER(artist)
                token = api_settings.JWT_ENCODE_HANDLER(payload)
                response = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER(
                    token, artist, request=request
                )
                return Response(response)
        return Response(
            {"detail": "Invalid credentials"},
            status=status.HTTP_401_UNAUTHORIZED
        )


class ArtistRegisterView(generics.CreateAPIView):

    permission_classes = [AnonPermissionOnly]
    serializer_class = ArtistSerializer
    passed_id = None
    queryset = Artist.objects.all()


class ArtistsDetailView(UpdateModelMixin, generics.DestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    lookup_field = 'id'

    # Update partial fields instead of whole object
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ArtistsDetailGetView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArtistDetailSerializer
    queryset = Artist.objects.all()
    lookup_field = 'id'


class ArtistsAdminListView(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = ArtistAdminSerializer
    passed_id = None
    # Filter
    search_fields = (
        'email', 'username', 'born_date',
        'origin', 'genre', 'is_admin',
        'is_staff', 'is_superuser', 'password'
    )
    ordering_fields = ('email', 'username', 'born_date',
                       'origin', 'genre', 'password')
    queryset = Artist.objects.all()

    # Returns a dict containing any extra context that should be supplied to serializer
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ArtistsAdminDetailView(generics.UpdateAPIView, generics.DestroyAPIView,
                             generics.RetrieveAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = ArtistAdminSerializer
    queryset = Artist.objects.all()
    lookup_field = 'id'

    # Update partial fields instead of whole object
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
