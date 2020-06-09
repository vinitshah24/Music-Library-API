from django import forms

from .models import Album as AlbumModel


class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = ['name']
