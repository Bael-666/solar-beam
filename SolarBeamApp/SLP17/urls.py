from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^new_usr/$', views.new_usr, name='new_usr'),
    url(r'^alta_usr/$', views.alta_usr, name='alta_usr'),
    url(r'^simulador/$', views.simulador, name='simulador'),
    url(r'^simulador/alta_cen/$', views.alta_cen, name='alta_cen'),
    url(r'^simulador/alta_cen/alta/$', views.alta_cen2, name='alta_cen2'),
#    url(r'^simulador/oferta/$', views.oferta, name='oferta'),
    url(r'^getNode/$', views.getNode, name="getNode"),
    url(r'^simulador/alta_paq/$', views.alta_paq1, name='alta_paq1'),
    url(r'^simulador/alta_paq/paq/$', views.alta_paq2, name='alta_paq2'),


]