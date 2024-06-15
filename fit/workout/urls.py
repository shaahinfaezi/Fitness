from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('shop',views.shop),
    path('blog',views.blog),
    path('free-workouts',views.free_workouts),
    path('plans/arm',views.arm),
    path('plans/back',views.back),
    path('plans/leg-day',views.leg),
    path('plans/chest-day',views.chest),
    path('plans/shoulder',views.shoulder),
]
