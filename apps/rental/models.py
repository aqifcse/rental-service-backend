from django.db import models

# Create your models here.
class Rental(models.Model):
    code = models.CharField(max_length=250)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=350)
    availability = models.BooleanField(null=True)
    needing_repair = models.BooleanField(null=True)
    durability = models.IntegerField(null=True)
    max_durability = models.IntegerField(null=True)
    max_durability = models.IntegerField(null=True)
    mileage = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    minimum_rent_period = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    estimated_price = models.IntegerField()
    booking_confirmed = models.BooleanField()

class Return(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.IntegerField()
    return_confirmed = models.BooleanField()


    

