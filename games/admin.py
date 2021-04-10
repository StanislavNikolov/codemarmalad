from django.contrib import admin
from .models import Game, Jam, Vote

@admin.register(Game)
class GameAdmin(admin.ModelAdmin): pass

@admin.register(Jam)
class JamAdmin(admin.ModelAdmin): pass

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin): pass
