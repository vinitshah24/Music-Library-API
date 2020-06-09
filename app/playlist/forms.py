from django import forms

from .models import Playlist as PlaylistModel


class PlaylistForm(forms.ModelForm):
    class Meta:
        model = PlaylistModel
        fields = ['name', 'song']
