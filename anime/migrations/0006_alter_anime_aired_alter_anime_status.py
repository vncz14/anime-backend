# Generated by Django 4.1.3 on 2022-11-22 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0005_remove_anime_anime_awards_anime_anime_awards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='status',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='anime',
            name='aired',
            field=models.DateField(null=True),
        ),
    ]
