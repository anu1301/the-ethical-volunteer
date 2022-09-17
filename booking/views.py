from django.shortcuts import render
# Generic views imported from django
from django.views import generic, View
# Product and Booking models imported from models.py
from .models import Product, Booking
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


class HomePage(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
            {'home_active': 'user-redirect'})


class HolidayView(View):
    template_name = "holiday.html"
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "holiday.html", 
            {"holiday_active": "user-redirect"})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Invalid login')
            else:
                form = LoginForm()
            return render(request, 'booking/login.html', {'form': form})
