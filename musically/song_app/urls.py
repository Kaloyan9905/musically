from django.urls import path, include

from musically.song_app.views import music_list, music_upload

urlpatterns = (
    path('list/', music_list, name='music list'),
    path('upload/', music_upload, name='music upload'),
)
