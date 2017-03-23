from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^resultados/$', views.resultados, name='resultados'),
    url(r'^simulador/$', views.simulador, name='simulador'),
    url(r'^simulador/alta/$', views.alta, name='alta'),
#    url(r'^simulador/oferta/$', views.oferta, name='oferta'),
    url(r'^getNode/$', views.getNode, name="getNode")    

]