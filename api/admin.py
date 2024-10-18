from django.contrib import admin
from .models import FuelStop


# Register your models here.
@admin.register(FuelStop)
class FuelStopAdmin(admin.ModelAdmin):
    # list_display = ["opis_truckstop_id", "truckstop_name", "address", "city", "state"]
    pass