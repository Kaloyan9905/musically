from random import choice

from django.contrib.auth import get_user_model
from django.core import exceptions as exceptions
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect
from musically.song_app.models import SongFile

UserModel = get_user_model()


class SongListView(views.ListView):
    model = SongFile
    template_name = 'song/list-songs.html'
    context_object_name = 'song_list'


class SongAddView(views.DetailView):
    model = SongFile
    template_name = 'song/list-songs.html'

    def get(self, request, *args, **kwargs):
        song = self.get_object()
        user_profile, created = UserModel.objects.get_or_create(email=self.request.user.email)
        user_profile.saved_songs.add(song)
        return redirect('list songs')


class SongEditView(views.UpdateView):
    model = SongFile
    template_name = 'song/edit-song.html'
    fields = ['title', 'artist', 'song_image_url', 'audio_file']
    success_url = reverse_lazy('list songs')


class SongDeleteView(views.DeleteView):
    model = SongFile
    template_name = 'song/delete-song.html'
    success_url = reverse_lazy('list songs')


class PersonalSongDeleteView(views.DeleteView):
    model = SongFile
    success_url = reverse_lazy('list songs')

    def get(self, request, *args, **kwargs):
        song = kwargs.get('pk')
        user_profile, created = UserModel.objects.get_or_create(email=self.request.user.email)
        user_profile.saved_songs.remove(song)
        return redirect('personal songs')


def music_upload(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        title = request.POST['title']
        artist = request.POST['artist']
        song_image_url = request.POST['image']
        audio_file = request.FILES['audio_file']

        SongFile.objects.create(
            title=title,
            artist=artist,
            audio_file=audio_file,
            song_image_url=song_image_url,
        )

        return render(request, 'music_player/upload-success.html')

    return render(request, 'music_player/music-upload.html')


def next_song_view(request, song_id):
    user_profile = __get_user_profile_by_email(request.user.email)

    next_song = user_profile \
        .saved_songs \
        .filter(pk__gt=song_id) \
        .order_by('pk') \
        .first()

    if next_song is None:
        next_song = user_profile \
            .saved_songs \
            .order_by('pk') \
            .first()

    context = {
        'song': next_song,
    }

    return render(request, 'music_player/music-player.html', context)


def previous_song_view(request, song_id):
    user_profile = __get_user_profile_by_email(request.user.email)

    previous_song = user_profile \
        .saved_songs \
        .filter(pk__lt=song_id) \
        .order_by('-pk') \
        .first()

    if previous_song is None:
        previous_song = user_profile \
            .saved_songs \
            .order_by('-pk') \
            .first()

    context = {
        'song': previous_song,
    }

    return render(request, 'music_player/music-player.html', context)


def personal_songs(request):
    user_profile = __get_user_profile_by_email(request.user.email)

    try:
        first_song_to_display = user_profile \
            .saved_songs \
            .filter(pk=__get_random_song_pk(user_profile)) \
            .get()

    except user_profile.saved_songs.model.DoesNotExist:
        first_song_to_display = None

    context = {
        'song': first_song_to_display,
    }

    return render(request, 'music_player/music-player.html', context)


def __get_random_song_pk(user_profile):
    try:
        existing_pks = user_profile \
            .saved_songs \
            .values_list('pk', flat=True)

        return choice(existing_pks)

    except IndexError:
        return None


def __get_user_profile_by_email(email):
    return UserModel \
        .objects \
        .get(email=email)
