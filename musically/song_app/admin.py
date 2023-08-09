from django.contrib import admin

from musically.song_app.models import SongFile, PersonalSongs


# Register your models here.
@admin.register(SongFile)
class SongFileAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'uploaded_at']
    search_fields = ['title', 'artist']
    list_filter = ['artist', 'uploaded_at']
    ordering = ['-uploaded_at']
    fields = ['title', 'artist', 'song_image_url', 'audio_file']
    list_per_page = 10
    date_hierarchy = 'uploaded_at'
    admin.site.site_title = 'My Music App Admin'
    admin.site.site_header = 'My Music App Administration'


@admin.register(PersonalSongs)
class PersonalSongsAdmin(admin.ModelAdmin):
    pass
