# Generated by Django 3.1.7 on 2021-03-30 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='cover_image',
            field=models.ImageField(upload_to=''),
        ),
    ]