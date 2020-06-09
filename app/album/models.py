from django.db import models

# Create your models here.
from django.db import models

from song.models import Song as SongModel


class Album(models.Model):
    name = models.CharField(max_length=100)
    song = models.ForeignKey(SongModel, on_delete=models.CASCADE)

    # def get_songs(self):
    #     print(self)
    #     return " ".join([s for s in self.song.all().get()])

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']
