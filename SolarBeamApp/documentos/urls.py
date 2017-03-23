from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^estudios/$', views.estudio1, name='estudio1'),
    url(r'^estudios/genestudio/$', views.genestudio1, name='genestudio1'),
]
