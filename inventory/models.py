from django.db import models


class Vehicle(models.Model):
    KILOMETERS = 'km'
    MILES = 'mi'
    mileage_choices = [
        (KILOMETERS, 'Kilometers'),
        (MILES, 'Miles')
    ]

    USED = 'used'
    NEW = 'new'
    condition_choices = [
        (USED, 'Used'),
        (NEW, 'New')
    ]

    GAS = 'gas'
    DIESEL = 'diesel'
    ELECTRIC = 'electric'
    engine_choices = [
        (GAS, 'Gas'),
        (DIESEL, 'Diesel'),
        (ELECTRIC, 'Electric')
    ]

    stock = models.BigAutoField(primary_key=True, verbose_name="Stock")
    branch = models.ForeignKey('users.Branch', on_delete=models.RESTRICT, verbose_name="Branch")

    vin = models.CharField(max_length=17, verbose_name='VIN')
    year = models.IntegerField(verbose_name='Year')
    make = models.CharField(max_length=30, verbose_name='Make')
    model = models.CharField(max_length=30, verbose_name='Model')
    trim = models.CharField(max_length=30, verbose_name='Trim')
    mileage = models.IntegerField(verbose_name='Mileage')
    mileage_units = models.CharField(choices=mileage_choices, default=KILOMETERS, max_length=2, verbose_name='Mileage Units')

    condition = models.CharField(max_length=4, choices=condition_choices, default=USED, verbose_name="Type")
    color = models.CharField(max_length=30, verbose_name='Color')
    body_style = models.CharField(max_length=20, null=True, blank=True, verbose_name='Body Style')
    body_type = models.CharField(max_length=20, null=True, blank=True, verbose_name='Body Type')
    engine_type = models.CharField(choices=engine_choices, default=GAS, max_length=8, verbose_name='Engine Type')

    def __str__(self):
        return '%d %s %s %s - %s' % (self.year, self.make, self.model, self.trim, self.vin[-6:])
