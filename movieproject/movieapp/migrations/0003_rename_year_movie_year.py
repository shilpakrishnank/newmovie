# Generated by Django 3.2.13 on 2022-08-04 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0002_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='Year',
            new_name='year',
        ),
    ]
