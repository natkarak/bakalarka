from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import KontaktForm, PostihForm

app_name= 'kompenz'
def index(request):
	
	return render(request, 'kompenz/index.html')


def dotaznik(request):
	
	return render(request, 'kompenz/dotaznik.html')

def odkazy(request):
	
	return render(request, 'kompenz/odkazy.html')

def kontakty(request):
	return render(request, 'kompenz/kontakty.html')

def kontakt_view(request):
	context = {'kontaktForm':KontaktForm()}
	if request.method == 'POST':
		form = KontaktForm(request.POST)
		if form.is_valid():
			predmet = form.cleaned_data['predmet']
			sprava = form.cleaned_data['sprava']
			odosielatel = form.cleaned_data['odosielatel']
			cc_myself = form.cleaned_data['cc_myself']

			prijemci = ['natka.rak@gmail.com']
			if cc_myself:
				prijemci.append(odosielatel)

			send_mail(predmet, sprava, odosielatel, prijemci)
			return HttpResponseRedirect('/thanks/')
	else:
		form = KontaktForm()
	context['kontaktForm'] = form
	return render(request, 'kompenz/kontakty.html', {'form':form})

def otazka1(request):


	return render(request, 'kompenz/otazka1.html')

def get_postih(request):
	if request.method == 'POST':
		form = PostihForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect ('/thanks/')
	else:
		form = PostihForm()

	return render(request, 'kompenz/otazka1.html', {'form': form})