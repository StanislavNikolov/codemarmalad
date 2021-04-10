import datetime

from django.forms import ModelForm
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Game, Vote


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
            return redirect('home')
        print(form.errors)
    else:
        form = GameForm()

    return render(request, 'games/upload.html', {'form': form})


def game(request, pk, slug=None): # slug is ignored
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game.html', {'game': game})


# TODO csfr token?
@login_required
def vote(request, pk, vtype):
    game = get_object_or_404(Game, pk=pk)
    try:
        score = Vote.VTYPE_TO_SCORE[vtype]
    except:
        return HttpResponse('')

    vote = Vote.objects.create(author=request.user, game=game, score=score)
    vote.save()

    return HttpResponse(score)
