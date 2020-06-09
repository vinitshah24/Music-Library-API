
from django.urls import path

from .views import ArtistsAdminListView, ArtistsAdminDetailView

urlpatterns = [
    path('', ArtistsAdminListView.as_view()),
    path('<id>', ArtistsAdminDetailView.as_view()),
]
