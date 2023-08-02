from django.contrib import admin

from musically.song_app.models import SongFile, PersonalSongs


# Register your models here.
@admin.register(SongFile)
class SongFileAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalSongs)
class PersonalSongsAdmin(admin.ModelAdmin):
    pass
