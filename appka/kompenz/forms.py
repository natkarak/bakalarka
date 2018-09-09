from django import forms
from .models import Postihnutie, KATPOS, OBLASTKOMP

class  KontaktForm(forms.Form):
	"""docstring for  ContactForm"""
	meno = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	sprava = forms.CharField(required = True, widget = forms.Textarea)

OTAZKA0 = (
	('opt1','áno - poznám svoju mieru postihu'),
	('opt2','nie - chcem ju zistiť podľa diagnózy'),
	)

class Otazka0Form(forms.Form):
	Chcete_zadať_mieru_postihu = forms.ChoiceField(choices = OTAZKA0, widget = forms.RadioSelect())

class Otazka1Form(forms.Form):
	Aké_máte_postihnutie = forms.ChoiceField(choices = KATPOS, widget = forms.RadioSelect())

OTAZKA2 = (
	('1', '1)	Centrálne neurogénne poruchy (poškodenie pyramídovej dráhy mozgu a miechy)'),
	('2', '2)	Periférne neurogénne poruchy (poškodenie periférnych nervov)'),
	('3', '3)	Cerebelárne poruchy'),
	('4', '4)	Extrapyramidové poruchy (Parkinsonský, choreatiformný, dystónny)'),
	('5', '5)	Kmeňové poruchy (závraty, synkopy, bulbárny syndróm)'),
	('6', '6)	Záchvatové poruchy'),
	('7', '7)	Diseminované poruchy CNS (demyelinizačné ochorenia a iné podobné zriedkavé ochorenia)'),
	('8', '8)	Difúzne poruchy CNS (encefalopatie rôznej etiológie)'),
	('9', '9)	Nádory lebkovej dutiny a miechového kanála'),
	)

class Otazka2Form(forms.Form):
	Aký_máte_druh_zdravotného_postihnutia = forms.ChoiceField(choices = OTAZKA2, widget = forms.RadioSelect())

OTAZKADiag = (
	('1','1)	ťažká monoparéza až monoplégia'),
	('2','2)	ťažká hemiparéza až hemiplégia'),
	('3','3)	ťažká paraparéza až paraplégia'),
	('4','4)	ťažká kvadruparéza až kvadruplégia'),
	('5','5)	monoparéza'),
	('6','6)	hemiparéza'),
	('7','7)	triparéza'),
	('8','8)	paraparéza'),
	('9','9)	kvadruparéza'),
	('10','10)	reziduálna paréza'),
	('11','11)	poruchy symbolických funkcií'),
	)
		
class OtazkaDiagForm(forms.Form):
	Ktorú_z_týchto_diagnóz_máte = forms.ChoiceField(choices = OTAZKADiag, widget = forms.RadioSelect())

OTAZKADiag2 = (
	('1','1) Porucha lícneho nervu'),
	('2','2) Periférne neurogénne poruchy hornej končatiny'),
	)

class OtazkaPerifNPForm(forms.Form):
	Ktorú_z_týchto_diagnóz_máte = forms.ChoiceField(choices = OTAZKADiag2, widget = forms.RadioSelect())

KOMPENZ = (
	('ano','áno'),
	('nie','nie'),
	)
class OtazkaKompForm(forms.Form):
	Chcete_pokračovať_zistením_nároku_na_kompenzácie = forms.ChoiceField(choices = KOMPENZ, widget = forms.RadioSelect())

class OblastKompForm(forms.Form):
	O_ktorú_oblasť_kompenzácie_máte_záujem = forms.ChoiceField(choices = OBLASTKOMP, widget = forms.RadioSelect)






















