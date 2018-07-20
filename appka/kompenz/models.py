from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Postihnutie (models.Model):
	nazov=models.CharField(max_length=200)
	druh=models.CharField(max_length=200)
	uroven=models.CharField(max_length=20) # uvoren = lahka, stredne tazka, tazka
	#miera=models.IntegerField(default=0)
	spodnaHranica=models.IntegerField(default = 0) # miera postihnutia v %
	hornaHranica=models.IntegerField(default = 100)
	def __str__(self):
		"""A function inside the class Postihnutie, to show the nazov"""
		return self.nazov