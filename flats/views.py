from django.views import generic
from .models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'flats/index.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Flat.objects.all()

class TenantGenView(generic.ListView):
    template_name = 'flats/tenant.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Tenant.objects.all()

class TenantCreate(CreateView):
    model = Tenant
    fields = ['tenant_nickname']

class CityGenView(generic.ListView):
    template_name = 'flats/city.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return City.objects.all()

class CityCreate(CreateView):
    model = City
    fields = ['city_name']

class FlatGenView(generic.ListView):
    template_name = 'flats/flat.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Flat.objects.all()


class FlatCreate(CreateView):
    model = Flat
    fields = ['city', 'address' ]

class RentGenView(generic.ListView):
    template_name = 'flats/rent.html'
    context_object_name = 'object_list'
    def get_queryset(self):
        return Rent.objects.all()

class RentCreate(CreateView):
    model = Rent
    fields = ['tenant', 'flat', 'rent_beginning', 'rent_end' ]


