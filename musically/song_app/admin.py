from django.contrib import admin

from musically.song_app.models import SongFile


# Register your models here.
@admin.register(SongFile)
class SongFileAdmin(admin.ModelAdmin):
    pass
