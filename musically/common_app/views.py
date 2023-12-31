from django.shortcuts import render, redirect

from musically.song_app.models import SongFile
from musically.song_app.views import personal_songs


# Create your views here.

def start_page(request):
    if request.user.is_authenticated:
        return redirect('personal songs')

    return render(request, 'common/start-page.html')


def home_page(request):
    return render(request, 'common/home-with-profile.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
