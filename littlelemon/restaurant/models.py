from django.db import models

# Create your models here.
# model for booking table

class Booking(models.Model):
    name = models.CharField(max_length=255, null=False)
    no_of_guest = models.IntegerField(name='no_of_guest', null=False)
    bookingdate = models.DateField(name='bookingdate', null=False)

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    inventory = models.IntegerField(null=False)

    def __str__(self):
        return self.name