from django.conf.urls import url, include, patterns


from rest_framework import routers
from . import views

# this gets our Foo model routed
router = routers.DefaultRouter()
router.register(r'foo', views.FooViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)), # Foo REST urls
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')), # browsable api login urls

)
