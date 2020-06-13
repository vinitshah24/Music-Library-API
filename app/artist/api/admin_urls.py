
from django.urls import path

from .views import ArtistsAdminListView, ArtistsAdminDetailView

urlpatterns = [
    path('', ArtistsAdminListView.as_view()),           # api/admin/artist/
    path('<id>', ArtistsAdminDetailView.as_view()),     # api/admin/artist/1
]
