# Generated by Django 4.1.5 on 2023-03-17 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0016_character_anime_anime_characters'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='season',
            field=models.CharField(max_length=255, null=True),
        ),
    ]