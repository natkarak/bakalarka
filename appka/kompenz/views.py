from django.http import HttpResponseRedirect
from django.forms import formset_factory
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy



from .forms import Otazka0Form, Otazka1Form, KontaktForm, Otazka2Form, OtazkaDiagForm, OtazkaPerifNPForm, OtazkaKompForm, OblastKompForm

app_name= 'kompenz'

def index(request):
	
	return render(request, 'kompenz/index.html')


def dotaznik(request):
	context = {'otazka0Form' : Otazka0Form()}
	if request.method == 'POST':
		form = Otazka0Form(request.POST)
		if form.is_valid():
			if form.cleaned_data['Chcete_zadať_mieru_postihu'] == 'opt2':  
				return HttpResponseRedirect('otazka1')
				#return render(request, 'kompenz/otazka1.html', {'otazka1form': Otazka1Form})
			else:
				return HttpResponseRedirect('kompenzacie')
	else:
		form = Otazka0Form()
		return render(request, 'kompenz/dotaznik.html', {'form': form})
		

def odkazy(request):
	
	return render(request, 'kompenz/odkazy.html')

def kontakty(request):
	form_class = KontaktForm
	return render(request, 'kompenz/kontakty.html', {'form':form_class})

def kompenzacie(request):
	context = {'OblastKompForm' : OblastKompForm()}
	if request.method == 'POST':
		form = OblastKompForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['O_ktorú_oblasť_kompenzácie_máte_záujem'] == 'a':  
				return HttpResponseRedirect('kompenzacie')
			elif form.cleaned_data['O_ktorú_oblasť_kompenzácie_máte_záujem'] == 'b':  
				return HttpResponseRedirect('kompenzacie')
			elif form.cleaned_data['O_ktorú_oblasť_kompenzácie_máte_záujem'] == 'c':  
				return HttpResponseRedirect('kompenzacie')
			else:
				return HttpResponseRedirect('odkazy')
	else:
		form = OblastKompForm()
	return render(request, 'kompenz/kompenzacie.html', {'form':form})

def otazka1(request):
	context = {'otazka1Form' : Otazka1Form()}
	if request.method == 'POST':
		form = Otazka1Form(request.POST)
		if form.is_valid():
			if form.cleaned_data['Aké_máte_postihnutie'] == '05':   
				return HttpResponseRedirect('otazka2')
			elif form.cleaned_data['Aké_máte_postihnutie'] == '12':
				return HttpResponseRedirect('odkazy')
	else:
		form = Otazka1Form()
	return render(request, 'kompenz/otazka1.html', {'form':form})

def otazka2(request):
	context = {'otazka2Form' : Otazka2Form()}
	if request.method == 'POST':
		form = Otazka2Form(request.POST)
		if form.is_valid():
			if form.cleaned_data['Aký_máte_druh_zdravotného_postihnutia'] == '1':
				return HttpResponseRedirect('otazkaDiag')
			elif form.cleaned_data['Aký_máte_druh_zdravotného_postihnutia'] == '2':
				return HttpResponseRedirect('otazkaPerifNP')
			#elif:

			else:
				return HttpResponseRedirect('odkazy')
	else:
		form = Otazka2Form()		
	return render(request, 'kompenz/otazka2.html', {'form':form})

def otazkaDiag(request):
	context = {'otazkaDiagForm' : OtazkaDiagForm()}
	if request.method == 'POST':
		form = OtazkaDiagForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '1':
				return HttpResponseRedirect('diag1')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '2':
				return HttpResponseRedirect('diag2')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '3':
				return HttpResponseRedirect('diag3')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '4':
				return HttpResponseRedirect('diag4')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '5':
				return HttpResponseRedirect('diag5')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '6':
				return HttpResponseRedirect('diag6')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '7':
				return HttpResponseRedirect('diag7')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '8':
				return HttpResponseRedirect('diag8')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '9':
				return HttpResponseRedirect('diag9')
			elif form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '10':
				return HttpResponseRedirect('diag10')
			else:
				return HttpResponseRedirect('diag11')	
	else:
		form = OtazkaDiagForm()
	return render(request, 'kompenz/otazkaDiag.html', {'form':form})

def diag1(request):
	return render(request, 'kompenz/diag1.html')
def diag2(request):
	return render(request, 'kompenz/diag2.html')
def diag3(request):
	return render(request, 'kompenz/diag3.html')
def diag4(request):
	return render(request, 'kompenz/diag4.html')
def diag5(request):
	return render(request, 'kompenz/diag5.html')
def diag6(request):
	return render(request, 'kompenz/diag6.html')
def diag7(request):
	return render(request, 'kompenz/diag7.html')
def diag8(request):
	return render(request, 'kompenz/diag8.html')
def diag9(request):
	context = {'OtazkaKompForm' : OtazkaKompForm()}
	if request.method == 'POST':
		form = OtazkaKompForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['Chcete_pokračovať_zistením_nároku_na_kompenzácie'] == 'ano':  
				return HttpResponseRedirect('kompenzacie')
			else:
				return HttpResponseRedirect('odkazy')
	else:
		form = OtazkaKompForm()
	return render(request, 'kompenz/diag9.html', {'form':form})
def diag10(request):
	return render(request, 'kompenz/diag10.html')
def diag11(request):
	return render(request, 'kompenz/diag11.html')

def otazkaPerifNP(request):
	context = {'otazkaPerifNPForm' : OtazkaPerifNPForm()}
	if request.method == 'POST':
		form = OtazkaDiagPerifNPForm(request.POST)
		if form.is_valid():
			if form.cleaned_data['Ktorú_z_týchto_diagnóz_máte'] == '1':
				return HttpResponseRedirect('diag')

	else:
		form = OtazkaPerifNPForm()
	return render(request, 'kompenz/otazkaPerifNP.html', {'form':form})

def otazkaDiag3(request):
	#
	return render(request, 'kompenz/otazkaDiag3.html')

def otazkaDiag4(request):
	#
	return render(request, 'kompenz/otazkaDiag4.html')

def otazkaDiag5(request):
	#
	return render(request, 'kompenz/otazkaDiag5.html')

def otazkaDiag6(request):
	#
	return render(request, 'kompenz/otazkaDiag6.html')

def otazkaDiag7(request):
	#
	return render(request, 'kompenz/otazkaDiag7.html')

def otazkaDiag8(request):
	#
	return render(request, 'kompenz/otazkaDiag8.html')

def otazkaDiag9(request):
	#
	return render(request, 'kompenz/otazkaDiag9.html')