from django import forms

class  KontaktForm(forms.Form):
	"""docstring for  ContactForm"""
	meno = forms.CharField(required = True)
	email = forms.EmailField(required = True)
	sprava = forms.CharField(required = True, widget = forms.Textarea)


OTAZKA1 = (
	('a', 'a.	Nervový systém (poškodenie mozgu, miechy a periférnych nervov'),
	('b', 'b.	Pohybový a podporný aparát'),
	)

class Otazka1Form(forms.Form):
	Aké_máte_postihnutie = forms.ChoiceField(choices = OTAZKA1, widget = forms.RadioSelect)
	
		





























