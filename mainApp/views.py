from django.db.models import F
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


class TransferRecordsView(View):
    def get(self, request):
        transferlar = Transfer.objects.all().order_by('-narx')
        context = {
            'transferlar': transferlar,
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




class ClubPlayersView(View):
    def get(self, request, club_id):
        club = Club.objects.get(id=club_id)
        players = Player.objects.filter(club=club)
        context = {
            'clubs': club,
            'players': players,
        }
        return render(request, 'clubplayers.html', context)



class ClubsXarajatView(View):
    def get(self, request):
        clublar = Club.objects.all()
        transfers = Transfer.objects.all()
        club_xarajat = {}
        for transfer in transfers:
            club = transfer.club2
            if club not in club_xarajat:
                club_xarajat[club] = 0
            club_xarajat[club] += transfer.narx
        eng_yuqori_50_clublar = sorted(club_xarajat.items(), key=lambda x: x[1], reverse=True)[:50]
        context = {
            'eng_yuqori_50_clublar': eng_yuqori_50_clublar
        }
        return render(request, 'stats/s.html', context)

class TransferAccurateView(View):
    def get(self, request):
        transfers = Transfer.objects.filter(narx=F('taxmin_narx'))
        context = {
            'transfers': transfers,
        }
        return render(request, "stats/150-accurate-predictions.html", context)


class ClubsDaromadView(View):
    def get(self, request):
        transfers = Transfer.objects.all()
        club_daromad = {}
        for transfer in transfers:
            club = transfer.club1
            if club not in club_daromad:
                club_daromad[club] = 0
            club_daromad[club] += transfer.narx
        eng_yuqori_50_clublar = sorted(club_daromad.items(), key=lambda x: x[1], reverse=True)[:50]
        context = {
            'eng_yuqori_50_clublar': [(club.id, club.nom, daromad) for club, daromad in eng_yuqori_50_clublar]
        }
        return render(request, 'stats/top-50-clubs-by-income-in-2021.html', context)




