"""
Definition of urls for SolarBeamDemo.
"""

from datetime import datetime
from django.conf.urls import include, url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from django.contrib.auth.views import login, logout
from django.contrib import admin
from SLP15.views import *

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about', about, name='about'),
    url(r'^solver$', solver, name='solver'),
    url(r'^login$',
        login,
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),
#    url(r'^reset/$', views.reset, name="password_reset"),
    url(r'^modelo1/', include('modelo1.urls')),
    url(r'^slp2015/', include('SLP15.urls')),
    url(r'^tarifas/', include('tarifas.urls')),
    url(r'^Solarbeam1.0/', include('Ciudades.urls')),
    url(r'^docs/', include('documentos.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^/slp2015/getNode/$', getNode, name="getNode")
    url('^', include('django.contrib.auth.urls')),
]
