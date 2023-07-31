from django.urls import reverse_lazy
from musically.song_app.models import SongFile
from django.views import generic as views


# Create your views here.

class SongListView(views.ListView):
    model = SongFile
    template_name = 'song/list-songs.html'
    context_object_name = 'song_list'


class SongEditView(views.UpdateView):
    model = SongFile
    template_name = 'song/edit-song.html'
    fields = ['title', 'artist', 'song_image_url', 'audio_file']
    success_url = reverse_lazy('list songs')


class SongDeleteView(views.DeleteView):
    model = SongFile
    template_name = 'song/delete-song.html'
    success_url = reverse_lazy('list songs')
