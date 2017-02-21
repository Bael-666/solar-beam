from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns = [
    url(r'^$modelo_whiskas', views.index, name='whiskas'),
]