from django.contrib import admin
from .models import Category, Product, Booking
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'price',
                    'available', 'created_on', 'updated')
    search_fields = ['name', 'content']
    list_filter = ['available', 'created_on', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('content')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'booking_id', 'user', 'booking_date', 'product_choice', 'duration',
        'status', 'created_on')
    list_filter = ('status', 'booking_date')
    readonly_fields = ('booking_id',)
    search_fields = ('booking_id', 'user')
    actions = ['approve_booking']

    def approve_booking(self, request, queryset):
        queryset.update(approve_booking=True)
