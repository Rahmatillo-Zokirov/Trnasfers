from pstats import Stats

from django.contrib import admin
from .models import *

from statsApp.models import *
class ClubAdmin(admin.ModelAdmin):
    search_fields = ('nom',)
    list_display = ('nom', 'logo', 'president', 'trener', 't_sana', 'kapital', 'davlat',)
    list_filter = ('davlat',)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('ism', 'club', 'pozitsiya')
    list_filter = ('club',)
    search_fields = ('club',)


admin.site.register(Club, ClubAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Mavsum)
admin.site.register(Transfer)
admin.site.register(Davlat)
admin.site.register(Pozitsiya)

