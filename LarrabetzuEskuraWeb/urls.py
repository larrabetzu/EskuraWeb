from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from rest_framework import routers
from Elkarteak.views import ElkarteakViewSet
from Ekintzak.views import EkintzakViewSet
from Blogak.views import BlogakViewSet
from Sarrerak.views import SarrerakViewSet

router = routers.DefaultRouter()
router.register(r'elkarteak', ElkarteakViewSet)
router.register(r'ekintzak', EkintzakViewSet)
router.register(r'blogak', BlogakViewSet)
router.register(r'sarrerak', SarrerakViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LarrabetzuEskuraWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
