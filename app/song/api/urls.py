from django.urls import path

from .views import SongListView, SongCreateView, SongDetailView

urlpatterns = [
    path('', SongListView.as_view()),
    path('create/', SongCreateView.as_view()),
    path('<id>', SongDetailView.as_view()),
]
