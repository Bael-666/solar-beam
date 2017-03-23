from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Solarbeam2/$', views.Solarbeam2, name='Solarbeam2'),
    url(r'^Solarbeam2/resumen/$', views.resumen, name='resumen'),
    url(r'^reporte/$', views.resultados, name='resultados'),
]
