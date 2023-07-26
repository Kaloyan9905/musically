from django.urls import path, include

from musically.song_app.views import music_list, music_upload, next_song_view, previous_song_view, song_details

urlpatterns = (
    path('list/', music_list, name='music list'),
    path('upload/', music_upload, name='music upload'),
    path('details/', song_details, name='song details'),
    path('next-song/<int:song_id>/', next_song_view, name='next song'),
    path('previous-song/<int:song_id>/', previous_song_view, name='previous song'),
)
