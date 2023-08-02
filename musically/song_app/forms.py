from django import forms

from musically.song_app.models import SongFile


class SongFileBaseForm(forms.ModelForm):
    class Meta:
        model = SongFile
        fields = '__all__'


class SongFileEditForm(SongFileBaseForm):
    class Meta:
        model = SongFile
        fields = ['title', 'artist', 'song_image_url', 'audio_file']
        widgets = {
            'audio_file': forms.HiddenInput(),
        }
