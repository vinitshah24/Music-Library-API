from django.urls import path

from .views import AlbumListView, AlbumCreateView, AlbumDetailView

urlpatterns = [
    path('', AlbumListView.as_view()),
    path('create/', AlbumCreateView.as_view()),
    path('<id>', AlbumDetailView.as_view()),
]
