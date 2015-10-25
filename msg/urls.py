from django.conf.urls import url, include, patterns
from rest_framework import routers

from . import views_page
from . import views

router = routers.DefaultRouter()
router.register(r'foo', views.FooViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)), # this includes all the urls for our Foo REST API
    url(r'^$', views_page.home, name="home"),
)
