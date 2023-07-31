from django.urls import path

from musically.album_app.views import SongListView, SongEditView, SongDeleteView

urlpatterns = (
    path('', SongListView.as_view(), name='list songs'),
    # path('songs/<int:pk>/add/', SongAddView.as_view(), name='add song'),
    path('edit/<int:pk>/', SongEditView.as_view(), name='edit song'),
    path('delete/<int:pk>/', SongDeleteView.as_view(), name='delete song'),
)
