from django.db import models

from artist.models import Artist as ArtistModel
from partial_date import PartialDateField


class Song(models.Model):
    name = models.CharField(max_length=100)
    year_released = PartialDateField()
    genre = models.CharField(max_length=100)
    artist = models.ForeignKey(ArtistModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['year_released']
