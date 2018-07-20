from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dotaznik', views.dotaznik, name='dotaznik'),
    url(r'^odkazy/', views.odkazy, name='odkazy'),
    url(r'^kontakty/', views.kontakty, name='kontakty'),
    url(r'^otazka1', views.otazka1, name='otazka1'),
]