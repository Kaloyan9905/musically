from django.shortcuts import render

from musically.song_app.models import SongFile


# Create your views here.

def start_page(request):
    if request.user.is_authenticated:
        home_page(request)

    return render(request, 'common/start-page.html')


def home_page(request):
    music_files = SongFile.objects.all()

    context = {
        'music_files': music_files,
    }

    return render(request, 'common/home-with-profile.html', context)


