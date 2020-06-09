
import json

from django.shortcuts import get_object_or_404

from rest_framework import generics, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication

from .serializers import ArtistSerializer, ArtistAdminSerializer
from artist.models import Artist as ArtistModel


class ArtistsListView(generics.ListCreateAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = ArtistSerializer
    passed_id = None
    # Filter
    search_fields = (
        'email', 'username', 'born_date',
        'origin', 'genre', 'is_admin'
    )
    ordering_fields = ('email', 'username', 'born_date',
                       'origin', 'genre')
    queryset = ArtistModel.objects.all()

    # Returns a dict containing any extra context that should be supplied to serializer
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ArtistsDetailView(generics.UpdateAPIView, generics.DestroyAPIView,
                        generics.RetrieveAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = ArtistSerializer
    queryset = ArtistModel.objects.all()
    lookup_field = 'id'


class ArtistsAdminListView(generics.ListCreateAPIView):

    authentication_classes = []
    permission_classes = []
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
    queryset = ArtistModel.objects.all()

    # Returns a dict containing any extra context that should be supplied to serializer
    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}


class ArtistsAdminDetailView(generics.UpdateAPIView, generics.DestroyAPIView,
                             generics.RetrieveAPIView):

    authentication_classes = []
    permission_classes = []
    serializer_class = ArtistAdminSerializer
    queryset = ArtistModel.objects.all()
    lookup_field = 'id'
