from django.shortcuts import render
# Generic views imported from django
from django.views import generic, View
# Product and Booking models imported from models.py
from .models import Product, Booking


class ProductList(generic.ListView):
    model = Product
    template_name = 'holiday.html'
    paginate_by = 6


# class HomePage(View):
#     template_name = 'index.html'

#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             'index.html',
#             {'home_active': 'user-redirect'})


# class HolidayView(View):
#     template_name = "holiday.html"
#     paginate_by = 6

#     def get(self, request, *args, **kwargs):
#         return render(
#             request,
#             "holiday.html", 
#             {"holiday_active": "user-redirect"})
