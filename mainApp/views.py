from django.shortcuts import render
from django.views import View

from django.conf import settings
from django.conf.urls.static import static

from mainApp.models import *
from statsApp.models import Transfer


class Home(View):
    def get(self, request):
        return render(request, 'index.html')

class About(View):
    def get(self, request):
        return render(request, 'about.html')

class Tryouts(View):
    def get(self, request):
        return render(request, 'tryouts.html')

class Clubs(View):
    def get(self, request):
        context = {
            'clublar': Club.objects.order_by('-kapital'),
        }
        return render(request, 'clubs.html', context)

class Players(View):
    def get(self, request):
        context = {
            'players': Player.objects.order_by('-ism'),
        }
        return render(request, 'players.html', context)

class Player_20(View):
    def get(self, request):
        all_players = Player.objects.all()
        player_20 = []
        for player in all_players:
            if player.yoshi() <= 20:
                player_20.append(player)
        context = {
            'players': player_20,
        }
        return render(request, 'U-20 players.html', context)


class LatestTransfer(View):
    def get(self, request):
        context = {
            'transferlar': Transfer.objects.all()
        }
        return render(request, "transfer-records.html", context)

class CountryClubsView(View):
    def get(self, request, pk):
        context = {
            'clubs': Club.objects.filter(davlat__id=pk),
            'davlat': Davlat.objects.get(id=pk),
        }
        return render(request, 'england.html', context)


class StatsView(View):
    def get(self, request):
        return render(request, 'stats.html')




class ClubPlayerView(View):
    def get(self, request, pk):
        club = Club.objects.get(id=pk)
        players = Player.objects.filter(club=club)
        context = {
            'clubs': club,
            'players': players,
        }
        return render(request, 'clubplyers.html', context)


class ClubsXarajatView(View):
    def get(self, request):
        clublar = Club.objects.all()
        trnsfer = Transfer.objects.all()
        club_xarajat = {}
        for club in clublar:
            club_xarajat.update({club.id:0})
            for t in trnsfer:
                if t.club2 == club:
                    club_xarajat.update({club.id:club_xarajat[club]+t.narx})
        return render(request, 'top-50-clubs-by-expenditure-in2021.html', club_xarajat)

