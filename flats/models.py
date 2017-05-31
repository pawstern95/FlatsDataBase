from django.db import models
from django.utils import timezone
import datetime
from django.db.models import Q
from django.db import IntegrityError


class Tenant(models.Model):
    tenant_nickname = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.tenant_nickname

class City(models.Model):
    city_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.city_name

class Flat(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    flat_id = models.CharField(max_length=10)
    rents = models.ManyToManyField(Tenant, through='Rent')
    rent_beginning = models.DateField('From', default=datetime.date.today)
    rent_end = models.DateField('To', default=datetime.date.today)

    def __str__(self):
        return self.flat_id


class Rent(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)
    rent_beginning = models.DateField('From', default=datetime.date.today)
    rent_end = models.DateField('To', default=datetime.date.today)

    # def __str__(self):
    #     return '%d - %d' % (self.rent_beginning, self.rent_end)

    def save(self, *args, **kwargs):
        if Rent.objects.filter(Q(flat=self.flat), Q(rent_beginning__range=(self.rent_beginning, self.rent_end)))\
                or Q(rent_end__range=(self.rent_beginning, self.rent_end)) \
                or Q(rent_beginning__lte=self.rent_beginning, rent_end__gte=self.rent_end):
            raise IntegrityError("Already occupied!!!")
        else:
            super(Rent, self).save()