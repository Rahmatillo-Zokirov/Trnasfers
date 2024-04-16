from django.db import models
from mainApp.models import *

class Mavsum(models.Model):
    nom = models.CharField(max_length=255)


    def __str__(self):
        return self.nom


class Transfer(models.Model):
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    club1 = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="esilar")
    club2 = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, related_name="yangilar")
    narx = models.PositiveSmallIntegerField()
    taxmin_narx = models.PositiveIntegerField()
    mavsum = models.ForeignKey(Mavsum, on_delete=models.SET_NULL, null=True)
    sana = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.player.ism

