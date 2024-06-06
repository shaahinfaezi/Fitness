from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def addWorkout(request):
    desc={
        "description":"3*15 squat"
        }
    Workout_Plan.insert_one(desc)
    return HttpResponse('added')

def getWorkouts(request):
    workouts=Workout_Plan.find()
    return HttpResponse(workouts)
