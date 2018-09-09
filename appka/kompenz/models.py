from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

KATPOS = (
		('05','Nervový systém (poškodenie mozgu, miechy a periférnych nervov)'),
		('12','Pohybový a podporný aparát'),
		)

class Postihnutie (models.Model):
	UROVENPOS = (
		('lah', 'ľahká'),
		('str', 'stredná'),
		('taz', 'ťažká'),
		)
	
	nazov =models.CharField(max_length=200)
	kategoria = models.CharField(max_length=2, choices = KATPOS)
	druh =models.CharField(max_length=200)
	uroven =models.CharField(max_length = 3, choices = UROVENPOS)
	spodnaHranica =models.IntegerField(default = 0) # miera postihnutia v %
	hornaHranica= models.IntegerField(default = 100)
	
	
	def __str__(self):
		"""A function inside the class Postihnutie, to show the nazov"""
		return self.nazov


OBLASTKOMP = (
	('a','a) mobility a orientácie'),
	('b','b) komunikácie'),
	('c','c) zvýšených výdavkov'),
	('d','d) sebaobsluhy'),
	)

class Kompenzacia(models.Model):

	nazov = models.CharField(max_length = 100)
	oblastKomp = models.CharField(max_length = 1, choices = OBLASTKOMP)
	dochodkovyVek = models.BooleanField(default = False)
	jednorazova = models.BooleanField()
	maxPrispevok = models.IntegerField(default = 100000)
	prijem = models.IntegerField(default = 350)

	def __str__(self):
		"""A function inside the class Postihnutie, to show the nazov"""
		return self.nazov

















