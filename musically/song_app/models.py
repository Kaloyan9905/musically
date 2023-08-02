from django.db import models


class SongFile(models.Model):
    title = models.CharField(
        max_length=100,
    )

    artist = models.CharField(
        max_length=100,
    )

    audio_file = models.FileField(
        upload_to='media/',
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    song_image_url = models.URLField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.title


class PersonalSongs(models.Model):
    pass
