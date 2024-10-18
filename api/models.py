from django.db import models

# Create your models here.
class FuelStop(models.Model):
    opis_truckstop_id = models.IntegerField()
    truckstop_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    rack_id = models.IntegerField()
    retail_price = models.DecimalField(max_digits=10, decimal_places=6)
    
    def __str__(self):
        return f"{self.truckstop_name}:\t {self.address}, {self.city}, {self.state}"