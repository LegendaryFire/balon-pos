from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import BigAutoField


class Branch(models.Model):
    location_code = BigAutoField(primary_key=True, verbose_name="Location Code")
    province = models.CharField(max_length=30, null=True, blank=True, verbose_name='Province')
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='City')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Address')
    postal_code = models.CharField(max_length=7, null=True, blank=True, verbose_name='Postal Code')
    phone_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='Phone Number')
    email_address = models.EmailField(max_length=254, null=True, blank=True, verbose_name='Email Address')
    pst_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='PST Number')
    dealer_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='Dealer Number')
    percent_pst = models.DecimalField(max_digits=8, decimal_places=2, default=6.0, verbose_name="PST (%)")
    percent_gst = models.DecimalField(max_digits=8, decimal_places=2, default=5.0, verbose_name="GST (%)")

    def __str__(self):
        return "%s" % self.city

    class Meta:
        verbose_name_plural = "Branches"


class User(AbstractUser):
    branch = models.ForeignKey('users.Branch', on_delete=models.RESTRICT, blank=True, null=True, verbose_name='Branch')
    auto_pst = models.BooleanField(default=False, verbose_name="Auto PST")
    auto_gst = models.BooleanField(default=True, verbose_name="Auto GST")
