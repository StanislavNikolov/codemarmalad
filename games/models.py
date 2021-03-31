from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    external_url = models.URLField()
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="cover_images/")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    upload_date = models.DateTimeField()

    def __str__(self):
        return f'game: {self.title}'
