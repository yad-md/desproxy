from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
#from proxy import views
#from desproxy import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'desproxy.views.home', name='home'),
    # url(r'^desproxy/', include('desproxy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

#   url(r'^server/$', 'proxy.views.server'),
   url(r'^server/(?P<server_id>\S+)?/?$', 'proxy.views.server'),
#   url(r'^domain/$', 'proxy.views.domain'),
   url(r'^domain/(?P<domain_id>\S+)/record/(?P<record_id>\S+)?/?$', 'proxy.views.record'),
   url(r'^domain/(?P<domain_id>\S+)?/?$', 'proxy.views.domain'),
   #url(r'^domain/(?P<domain_id>\[0-9a-z-]+)/$', 'proxy.views.domain'),
   #url(r'^domain/(?P<domain_id>\S+)/record/$', 'proxy.views.record'),
   #url(r'^domain/(?P<domain_id>\S+)/record/(?P<record_id>\S+)$', 'proxy.views.record'),
#  url(r'^.*$', 'desproxy.views.proxy'),
)
