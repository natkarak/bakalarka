from django import forms

from .models import Postihnutie

class KontaktForm(forms.Form):
	predmet = forms.CharField(max_length=100)
	sprava = forms.CharField(widget = forms.Textarea)
	odosielatel = forms.EmailField()
	cc_myself = forms.BooleanField(required = False)







AKY_POSTIH= [
    ('nervove', 'a.	Nervový systém (poškodenie mozgu, miechy a periférnych nervov)'),
    ('pohyb', 'b.	Pohybový a podporný aparát'),
    ]

class PostihForm(forms.Form):    
	akyPostih = forms.CharField(label = 'Aké máte postihnutie?', widget = forms.RadioSelect(choices = AKY_POSTIH))
































