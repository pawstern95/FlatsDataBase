from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Q
from django.db import IntegrityError
from django.core.urlresolvers import reverse


class Tenant(models.Model):
    tenant_nickname = models.CharField(max_length=40, unique=True)

    def get_absolute_url(self):
        return reverse('flats:tenant')

    def __str__(self):
        return self.tenant_nickname

class City(models.Model):
    city_name = models.CharField(max_length=20, unique=True)

    def get_absolute_url(self):
        return reverse('flats:city')

    def __str__(self):
        return self.city_name


class Flat(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    rents = models.ManyToManyField(Tenant, through='Rent')

    def get_absolute_url(self):
        return reverse('flats:flat')

    def __str__(self):
        return ('%s - %s') % (self.city.city_name, self.address)

class Availability(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, default='')
    day = models.DateField(default=datetime.date.today)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return '%s - %s - %s' % (self.flat, self.day, self.availability)


class Rent(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    rent_beginning = models.DateField('From', default=datetime.date.today)
    rent_end = models.DateField('To', default=datetime.date.today)

    def get_absolute_url(self):
        return reverse('flats:rent')

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.tenant.tenant_nickname, self.flat.city.city_name, self.flat.address,
                                           self.rent_beginning, self.rent_end)






