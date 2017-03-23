from django.conf.urls import url

from . import views
app_name = 'tarifas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tarifa1/$', views.tarifa1, name='tarifa1'),
    url(r'^dac/$', views.dac, name='dac'),
    url(r'^tarifa1/(?P<ciudades_id>[0-9]+)/$', views.detalles, name='detalles'),
    url(r'^tarifa2/$', views.tarifa2, name='tarifa2'),
    url(r'^tarifa2/energia/$', views.t2energia, name='t2energia'),
    url(r'^dac/(?P<areascontrol_id>[0-9]+)/$', views.dac2, name='dac2'),
]