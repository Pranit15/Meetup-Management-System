from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='all-meetups'), # domain our-website.com/meetups
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail') # our-website/meetups/(a-first-meetup or a-second-meetup) 
]