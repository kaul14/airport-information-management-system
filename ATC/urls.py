from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
app_name='ATC'

urlpatterns = [
    path('accounts/login/',auth_views.LoginView, name='login'),
    path('',views.LoginView,name='login_page'),
    path('home/',views.HomeView,name='home_page'),
    path('new_operator/',views.OperatorView,name='new_operator'),
    path('aircraft_type/',views.AircraftTypeView,name='aircraft_type'),
    path('location/',views.LocationView,name='location'),
    path('aircraft_new/',views.AircraftNewView,name='aircraft_new'),
    path('schedule_flight/',views.ScheduleView,name='schedule_flight'),
    path('schedule_departure/',views.ScheduleDepartureView,name='schedule_departure'),
    path('schedule_arrival/',views.ScheduleArrivalView,name='schedule_arrival'),
    path('display/',views.DisplayView,name='display'),
# django.contrib.auth.views.LoginView



]
