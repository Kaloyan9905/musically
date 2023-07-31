from django.contrib import admin

from musically.album_app.models import PersonalSongs


# Register your models here.

@admin.register(PersonalSongs)
class PersonalSongsAdmin(admin.ModelAdmin):
    pass
