from django.conf.urls import url

from . import views

app_name = 'flats'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'flat/$', views.FlatGenView.as_view(), name='flat'),
    url(r'tenant/$', views.TenantGenView.as_view(), name='tenant'),
    url(r'city/$', views.CityGenView.as_view(), name='city'),
    url(r'rent/$', views.RentGenView.as_view(), name='rent'),
    url(r'tenant/add/$', views.TenantCreate.as_view(), name='tenant-add'),
    url(r'city/add/$', views.CityCreate.as_view(), name='city-add'),
    url(r'flat/add/$', views.FlatCreate.as_view(), name='flat-add'),
    url(r'rent/add/$', views.RentCreate.as_view(), name='rent-add'),
]