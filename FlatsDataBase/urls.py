from django.conf.urls import include, url
from django.contrib import admin
from flats import views

urlpatterns = [
    url(r'^flats/', include('flats.urls')),
    url(r'^admin/', admin.site.urls),

]