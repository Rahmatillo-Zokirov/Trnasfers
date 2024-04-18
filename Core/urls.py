from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from mainApp.views import *
from statsApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name="home"),
    path('about/', About.as_view(), name='about'),
    path('tryouts/', Tryouts.as_view(), name='tr'),
    path('clublar/', Clubs.as_view(), name='clublar'),
    path('davlatlar/<int:pk>/clubs/', CountryClubsView.as_view(), name='clublars'),
    path('transfers/', LatestTransfers.as_view(), name='transfers'),
    path('players/', Players.as_view(), name='players'),
    path('player_20/', Player_20.as_view(), name='player_20'),
    path('transfers_r/', TransferRecordsView.as_view(), name='transfers_r'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('clubs/<int:club_id>/players/', ClubPlayersView.as_view(), name='club_players'),
    path('accurate/', TransferAccurateView.as_view(), name='accurate_predictions'),
    path('top-50-clubs/', ClubsXarajatView.as_view(), name='top_50_clubs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
