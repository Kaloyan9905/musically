from random import choice

from django.shortcuts import render

from musically.song_app.models import SongFile


# Create your views here.

def music_upload(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        title = request.POST['title']
        artist = request.POST['artist']
        audio_file = request.FILES['audio_file']

        SongFile.objects.create(
            title=title,
            artist=artist,
            audio_file=audio_file,
        )

        return render(request, 'music_player/upload-success.html')

    return render(request, 'music_player/music-upload.html')


def music_list(request):
    music_files = SongFile.objects.all()
    return render(request, 'music_player/music-list.html', {'music_files': music_files})


def next_song_view(request, song_id):
    next_song = SongFile \
        .objects \
        .filter(pk__gt=song_id) \
        .order_by('pk'). \
        first()

    if next_song is None:
        next_song = SongFile \
            .objects \
            .order_by('pk') \
            .first()

    context = {
        'song': next_song,
    }

    return render(request, 'music_player/music-player.html', context)


def previous_song_view(request, song_id):
    previous_song = SongFile \
        .objects \
        .filter(pk__lt=song_id) \
        .order_by('-pk') \
        .first()

    if previous_song is None:
        previous_song = SongFile \
            .objects. \
            order_by('-pk') \
            .first()

    context = {
        'song': previous_song,
    }

    return render(request, 'music_player/music-player.html', context)


def song_details(request):
    first_song = SongFile \
        .objects \
        .filter(pk=__get_random_song_pk()) \
        .get()

    context = {
        'song': first_song,
    }

    return render(request, 'music_player/music-player.html', context)


def __get_random_song_pk():
    existing_pks = SongFile \
        .objects \
        .values_list('pk', flat=True)

    return choice(existing_pks)
