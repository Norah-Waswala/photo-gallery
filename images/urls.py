from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.landing,name = 'landing'),
    url(r'^location/(?P<location>\w+)/', views.image_location, name='location'),
    
    url(r'^search/', views.search_results, name='search'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)