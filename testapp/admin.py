from django.contrib import admin

# Register your models here.
from .models import Country, Schools


admin.site.register(Country)
admin.site.register(Schools)
