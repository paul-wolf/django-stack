from django.conf.urls import include, url
from django.contrib import admin
from msg import urls, views_page
from msg import urls_api

urlpatterns = [

    url(r'^$', views_page.home, name="home"),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
    url('^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/',include(urls_api)),
    url(r'^msg/',include(urls)),
]
