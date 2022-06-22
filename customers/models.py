from django.db import models


class Customer(models.Model):
    customer_number = models.BigAutoField(primary_key=True, verbose_name="ID")
    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    province = models.CharField(max_length=30, null=True, blank=True, verbose_name='Province')
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='City')
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name='Address')
    postal_code = models.CharField(max_length=7, null=True, blank=True, verbose_name='Postal Code')
    phone_number = models.CharField(max_length=16, null=True, blank=True, verbose_name='Phone Number')
    email_address = models.EmailField(null=True, blank=True, verbose_name='Email Address')
    gst_number = models.CharField(max_length=50, null=True, blank=True, verbose_name='GST Number')
    notes = models.CharField(max_length=254, null=True, blank=True, verbose_name='Additional Information')
