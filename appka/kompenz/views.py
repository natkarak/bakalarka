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
	context = formset_factory(Otazka0Form)
	if request.method == 'POST':
		formset = context(request.POST)
		if formset.is_valid():
			if formset.cleaned_data[0] == 'opt2':
				return HttpResponseRedirect('kontakty')
			else:
				return HttpResponseRedirect('odkazy')
	else:
		formset = context()
		return render(request, 'kompenz/dotaznik.html', {'formset': formset})
		

def odkazy(request):
	
	return render(request, 'kompenz/odkazy.html')

def kontakty(request):
	form_class = KontaktForm
	return render(request, 'kompenz/kontakty.html', {'form':form_class})


def otazka1(request):
	form_class = Otazka1Form
	return render(request, 'kompenz/otazka1.html'), #{'form':form_class})



