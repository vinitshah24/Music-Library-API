
from django.urls import path

from .views import (ArtistsListView, ArtistsDetailView, ArtistsDetailGetView, ArtistRegisterView )

urlpatterns = [
    path('', ArtistsListView.as_view()),                   # api/artist/
    path('register/', ArtistRegisterView.as_view()),       # api/artist/register
    path('id/<id>', ArtistsDetailGetView.as_view()),       # api/artist/id/1
    path('<id>', ArtistsDetailView.as_view()),             # api/artist/1
]
