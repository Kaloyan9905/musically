from django.urls import path

from musically.album_app.views import SongListView, SongEditView, SongDeleteView

urlpatterns = (
    path('songs/', SongListView.as_view(), name='list songs'),
    # path('songs/<int:pk>/add/', SongAddView.as_view(), name='add song'),
    path('songs/<int:pk>/edit/', SongEditView.as_view(), name='edit song'),
    path('songs/<int:pk>/delete/', SongDeleteView.as_view(), name='delete song'),
)
