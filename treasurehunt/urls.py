from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static
from login.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'treasurehunt.views.home', name='home'),
    # url(r'^treasurehunt/', include('treasurehunt.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',index),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^facebook/', include('django_facebook.urls')),
	url(r'^accounts/', include('django_facebook.auth_urls')),
	url(r'^treasure/$',register_next),
    url(r'^next/$',next),
 #Don't add this line if you use django registration or userena for registration and auth.
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
