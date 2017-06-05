from django.contrib import admin
from .models import *

admin.site.register(Tenant)
admin.site.register(City)
admin.site.register(Flat)
admin.site.register(Rent)
admin.site.register(Availability)

