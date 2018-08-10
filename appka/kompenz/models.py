from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Postihnutie (models.Model):
	nazov =models.CharField(max_length=200)
	kategoria = models.CharField(max_length=200, default = 'postih')
	druh =models.CharField(max_length=200)
	uroven =models.CharField(max_length=20) # uvoren = lahka, stredne tazka, tazka
	spodnaHranica =models.IntegerField(default = 0) # miera postihnutia v %
	hornaHranica= models.IntegerField(default = 100)

	NERVOVE = 'NS'
	POHYBOVE = 'PH'

	KATEGORIA_POSTIH = (
		(NERVOVE, 'Nervový systém - poškodenie mozgu, miechy a periférnych nervov'),
		(POHYBOVE, 'Pohybový a podporný systém')
	)

	kategoria_postih = models.CharField( max_length = 2, choices = KATEGORIA_POSTIH)
	
	def is_upperclass(self):
		return self.kategoria_postih in (self.NERVOVE, self.POHYBOVE)

	def __str__(self):
		"""A function inside the class Postihnutie, to show the nazov"""
		return self.nazov

class Osoba (models.Model):
	meno = models.CharField(max_length = 100)
	priezvisko = models.CharField(max_length = 150)
	postihnutie = models.ForeignKey(Postihnutie, on_delete = models.SET_NULL, null = True)
	
	def __str__(self):
		"""A function inside the class Postihnutie, to show the nazov"""
		return self.meno
	#prijem = models.IntegerField(default = 0)
	#neplnolety = models.BooleanField(default = False)
	#prodiktivnyVek = models.BooleanField()

class Kompenzacia(models.Model):
	nazov = models.CharField(max_length = 100)
	oblastKomp = models.CharField(max_length = 200)


	def __str__(self):
		"""A function inside the class Postihnutie, to show the nazov"""
		return self.nazov

















