from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$',views.landing,name = 'landing'),
    url(r'^single/(\d+)',views.single,name ='single'),
    url(r'^location/',views.image_location,name='location')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)