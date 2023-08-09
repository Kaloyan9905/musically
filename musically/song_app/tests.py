from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from musically.song_app.models import SongFile
from musically.song_app.views import previous_song_view, personal_songs, next_song_view, music_upload

UserModel = get_user_model()


class SongViewsTestCase(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create_user(username='testuser', password='testpassword')
        self.song = SongFile.objects.create(title='Test Song', artist='Test Artist')

    def test_song_list_view(self):
        url = reverse('list songs')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song/list-songs.html')
        self.assertIn(self.song, response.context['song_list'])

    def test_song_add_view(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('add song', kwargs={'pk': self.song.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Should redirect after adding the song
        # You can add further assertions to verify that the song was added to the user's saved_songs.

    def test_song_edit_view(self):
        url = reverse('edit song', kwargs={'pk': self.song.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song/edit-song.html')
        # You can add further assertions to verify the form fields and editing functionality.

    def test_song_delete_view(self):
        url = reverse('delete song', kwargs={'pk': self.song.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'song/delete-song.html')
        # You can add further assertions to verify the delete functionality.
