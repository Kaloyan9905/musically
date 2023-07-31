from django.db import models

from musically.song_app.models import SongFile


# Create your models here.

class PersonalSongs(models.Model):
    song = models.ManyToManyField(
        SongFile,
    )
