# Generated by Django 4.2.3 on 2023-08-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_app', '0005_remove_personalsongs_song'),
        ('auth_app', '0004_delete_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='saved_songs',
            field=models.ManyToManyField(to='song_app.songfile'),
        ),
    ]
