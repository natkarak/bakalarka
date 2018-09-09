from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dotaznik', views.dotaznik, name='dotaznik'),
    url(r'^odkazy/', views.odkazy, name='odkazy'),
    url(r'^kontakty/', views.kontakty, name='kontakty'),
    url(r'^kompenzacie/', views.kompenzacie, name='kompenzacie'), 
    url(r'^otazka1', views.otazka1, name='otazka1'),
    url(r'^otazka2', views.otazka2, name='otazka2'),
    url(r'^otazkaDiag', views.otazkaDiag, name='otazkaDiag'),
    url(r'^diag1', views.diag1, name='diag1'),
    url(r'^diag2', views.diag2, name='diag2'),
    url(r'^diag3', views.diag3, name='diag3'),
    url(r'^diag4', views.diag4, name='diag4'),
    url(r'^diag5', views.diag5, name='diag5'),
    url(r'^diag6', views.diag6, name='diag6'),
    url(r'^diag7', views.diag7, name='diag7'),
    url(r'^diag8', views.diag8, name='diag8'),
    url(r'^diag9', views.diag9, name='diag9'),
    url(r'^diag10', views.diag10, name='diag10'),
    url(r'^diag11', views.diag11, name='diag11'), 
    url(r'^otazkaPerifNP', views.otazkaPerifNP, name='otazkaPerifNP'),   
    url(r'^otazkaDiag3', views.otazkaDiag3, name='otazkaDiag3'),
    url(r'^otazkaDiag4', views.otazkaDiag4, name='otazkaDiag4'),
    url(r'^otazkaDiag5', views.otazkaDiag5, name='otazkaDiag5'),
    url(r'^otazkaDiag6', views.otazkaDiag6, name='otazkaDiag6'),
    url(r'^otazkaDiag7', views.otazkaDiag7, name='otazkaDiag7'),
    url(r'^otazkaDiag8', views.otazkaDiag8, name='otazkaDiag8'),
    url(r'^otazkaDiag9', views.otazkaDiag9, name='otazkaDiag9'),
    
]
