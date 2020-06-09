from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

from song.models import Song as SongModel


class Playlist(models.Model):
    name = models.CharField(max_length=100)
    song = models.ManyToManyField(SongModel)

    def __str__(self):
        return str(self.name)
