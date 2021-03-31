import datetime

from django.shortcuts import render
from django.forms import ModelForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .models import Game


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'external_url', 'cover_image']


def index(request):
    games = Game.objects.all().order_by('-upload_date')
    return render(request, 'games/index.html', {'games': games})

@login_required
def upload(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            new_game = form.save(commit=False)
            new_game.author = request.user
            new_game.upload_date = datetime.datetime.now()
            new_game.save()
            return # TODO forward to game page
        print(form.errors)
    else:
        form = GameForm()

    return render(request, 'games/upload.html', {'form': form})