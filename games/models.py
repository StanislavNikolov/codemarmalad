from django.db import models
from accounts.models import User


class Game(models.Model):
    external_url = models.URLField()
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="cover_images/")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    upload_date = models.DateTimeField()

    def count_upvotes(self):
        return self.vote_set.filter(score=Vote.VTYPE_TO_SCORE['up']).count()

    def count_downvotes(self):
        return self.vote_set.filter(score=Vote.VTYPE_TO_SCORE['down']).count()

    def __str__(self):
        return f'game: {self.title}'


class Jam(models.Model):
    name = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    tiny_image = models.ImageField("jam_images/")
    description_html = models.TextField()
    publicly_lsited = models.BooleanField(default=False)

    def __str__(self):
        return f'jam: {self.name}'


class Vote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    score = models.IntegerField()

    VTYPE_TO_SCORE = { 'up': +1, 'down': -1 }

    def __str__(self):
        return f'Vote {self.score} from @{self.author.username} for "{self.game.title}"'
