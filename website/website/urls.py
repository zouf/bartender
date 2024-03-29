from django.conf.urls import patterns, include, url
from bartender import views as barviews
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^website/', include('website.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^load', barviews.load, name='load'),
    url(r'^bar', barviews.bar, name='bar'),
    url(r'^order_drink', barviews.order_drink, name='order_drink'),
    url(r'^announce', barviews.announce, name='announce'),
    url(r'^make_drink', barviews.make_drink, name='make_drink'),    
    url(r'^mix_drink', barviews.mix_drink, name='mix_drink'),        
)

urlpatterns += staticfiles_urlpatterns()