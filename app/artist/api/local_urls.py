
from django.urls import path

from .views import ArtistsListView, ArtistsDetailView

urlpatterns = [
    path('', ArtistsListView.as_view()),
    path('<id>', ArtistsDetailView.as_view()),
]
