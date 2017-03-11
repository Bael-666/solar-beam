from django.conf.urls import url

from . import views
app_name = 'tarifas'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<ciudades_id>[0-9]+)/$', views.detalles, name='detalles'),
]