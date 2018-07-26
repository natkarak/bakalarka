from django import forms

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
	Chcete_zadať_mieru_postihu = forms.ChoiceField(choices = OTAZKA0, widget = forms.RadioSelect)


		
OTAZKA1 = (
	('a', 'a.	Nervový systém (poškodenie mozgu, miechy a periférnych nervov'),
	('b', 'b.	Pohybový a podporný aparát'),
	)

class Otazka1Form(forms.Form):
	Aké_máte_postihnutie = forms.ChoiceField(choices = OTAZKA1, widget = forms.RadioSelect)




























