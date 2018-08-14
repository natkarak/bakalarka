from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Osoba

from .forms import Otazka0Form, Otazka1Form, KontaktForm

app_name= 'kompenz'

def index(request):
	
	return render(request, 'kompenz/index.html')


def dotaznik(request):
	context = {'otazka0Form' : Otazka0Form()}
	if request.method == 'POST':
		form = Otazka0Form(request.POST)
		if form.is_valid():
			if form.cleaned_data['Chcete_zadať_mieru_postihu'] == 'opt2':   #[0] vyberie prvy form zo zoznamu, lebo formset_factory je zoznam formov a nema cleaned_data
				return render(request, 'kompenz/otazka1.html')
			else:
				return HttpResponseRedirect('odkazy')
	else:
		form = Otazka0Form()
		return render(request, 'kompenz/dotaznik.html', {'form': form})
		

def odkazy(request):
	
	return render(request, 'kompenz/odkazy.html')

def kontakty(request):
	form_class = KontaktForm
	return render(request, 'kompenz/kontakty.html', {'form':form_class})


def otazka1(request):
	context = {'otazka1Form' : Otazka1Form()}
	if request.method == 'POST':
		form = Otazka1Form(request.POST)
		if form.is_valid():
			if form.cleaned_data['Aké_máte_postihnutie'] == 'opt2':   #[0] vyberie prvy form zo zoznamu, lebo formset_factory je zoznam formov a nema cleaned_data
				return HttpResponseRedirect('kontakty')
			else:
				return HttpResponseRedirect('odkazy')
	else:
		form = Otazka1Form()
	return render(request, 'kompenz/otazka1.html', {'form':form})



