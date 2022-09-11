from django.shortcuts import render
from django.views import generic, View
from .models import Product, Booking

# Create your views here.


class HomePage(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'home_active': 'user-redirect'})


class HolidayView(View):
    template_name = "holiday.html"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        return render(request, "holiday.html", {"holiday_active": "custom-red",})

