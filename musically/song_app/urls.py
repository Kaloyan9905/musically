from django.urls import path

from musically.song_app.views import music_upload, next_song_view, previous_song_view, personal_songs, \
    SongListView, SongEditView, SongDeleteView, SongAddView

urlpatterns = (
    path('upload/', music_upload, name='music upload'),
    path('details/', personal_songs, name='personal songs'),
    path('next-song/<int:song_id>/', next_song_view, name='next song'),
    path('previous-song/<int:song_id>/', previous_song_view, name='previous song'),
    path('list/', SongListView.as_view(), name='list songs'),
    path('add/<int:pk>', SongAddView.as_view(), name='add song'),
    path('edit/<int:pk>/', SongEditView.as_view(), name='edit song'),
    path('delete/<int:pk>/', SongDeleteView.as_view(), name='delete song'),
)
