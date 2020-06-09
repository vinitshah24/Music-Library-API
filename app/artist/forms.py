from django import forms

from .models import Artist as ArtistModel


class ArtistForm(forms.ModelForm):
    class Meta:
        model = ArtistModel
        fields = [
            'email', 'username', 'born_date',
            'origin', 'genre', 'is_admin',
            'is_staff', 'is_superuser'
        ]
