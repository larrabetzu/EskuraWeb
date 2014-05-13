from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework import routers
from Elkarteak.views import ElkarteaViewSet

router = routers.DefaultRouter()
router.register(r'elkarteak', ElkarteaViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LarrabetzuEskuraWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
