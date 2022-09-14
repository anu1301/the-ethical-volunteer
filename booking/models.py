from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

DURATION = ((7, "7 Days"), (14, "14 Days"), (21, "21 Days"))
STATUS = ((0, 'Booking Made'), (1, 'Booking Confirmed'))
PRODUCTLIST = ()


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
  
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    available = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return str(self.name)


class Booking(models.Model):
    booking_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking")
    product_choice = models.ForeignKey(
        Product, on_delete=models.CASCADE, max_length=100, related_name='product_list')
    booking_date = models.DateField(auto_now=False)
    created_on = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=10, choices=DURATION, default='7')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-booking_date']
