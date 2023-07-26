from django.shortcuts import render

from musically.song_app.models import SongFile


# Create your views here.

def music_upload(request):
    if request.method == 'POST' and request.FILES['audio_file']:
        title = request.POST['title']
        artist = request.POST['artist']
        audio_file = request.FILES['audio_file']
        SongFile.objects.create(title=title, artist=artist, audio_file=audio_file)
        return render(request, 'music_player/upload_success.html')

    return render(request, 'music_player/music_upload.html')


def music_list(request):
    music_files = SongFile.objects.all()
    return render(request, 'music_player/music_list.html', {'music_files': music_files})
