from django import forms

from .models import Song as SongModel


class SongForm(forms.ModelForm):
    class Meta:
        model = SongModel
        fields = ['name', 'year_released', 'genre', 'artist']
