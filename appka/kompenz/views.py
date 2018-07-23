from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Otazka1Form, KontaktForm

app_name= 'kompenz'

def index(request):
	
	return render(request, 'kompenz/index.html')


def dotaznik(request):
	
	return render(request, 'kompenz/dotaznik.html')

def odkazy(request):
	
	return render(request, 'kompenz/odkazy.html')

def kontakty(request):
	form_class = KontaktForm
	return render(request, 'kompenz/kontakty.html', {'form':form_class})


def otazka1(request):
	form_class = Otazka1Form
	return render(request, 'kompenz/otazka1.html', {'form':form_class})
