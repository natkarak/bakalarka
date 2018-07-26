from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Otazka0Form, Otazka1Form, KontaktForm

app_name= 'kompenz'

def index(request):
	
	return render(request, 'kompenz/index.html')


def dotaznik(request):
	context = {'otazka0Form' : Otazka0Form()}
	if request.method == 'GET': 
		form = Otazka0Form(request.GET)
		zad_postih = request.GET.get('zad_postih')
		if 'zad_postih' == 'opt1':
			return HttpResponseRedirect('kompenz/otazka1.html')
		elif 'zad_postih' == 'opt2':
			return HttpResponseRedirect('kompenz/kontakty.html')
	else:
		form = Otazka0Form()
	#context['otazka0Form'] = form
	#form_class = Otazka0Form
	#Chcete_zadať_mieru_postihu = data.get('OTAYZKA0')
	return render(request, 'kompenz/dotaznik.html', {'form':form})

def odkazy(request):
	
	return render(request, 'kompenz/odkazy.html')

def kontakty(request):
	form_class = KontaktForm
	return render(request, 'kompenz/kontakty.html', {'form':form_class})


def otazka1(request):
	form_class = Otazka1Form
	return render(request, 'kompenz/otazka1.html', {'form':form_class})
