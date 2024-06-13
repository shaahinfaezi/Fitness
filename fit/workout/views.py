from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from forms import LogWorkout
# Create your views here.

def index(request):
    return render(request,"index.html",{})
def about(request):
    return render(request,"about.html",{})
def contact(request):
    if request.method == "POST":
        Muscle_group=request.POST.get("Muscle-Group")
        Year=request.POST.get("field")
        Month=request.POST.get("field-2")
        Day=request.POST.get("field-3")
        Description=request.POST.get("Write-your-sets")
        dic={"Muscle_group":Muscle_group,
             "Year":Year,
             "Month":Month,
             "Day":Day,
             "Description":Description
             }
        Workout_Plan.insert_one(dic)
    return render(request,"contact.html",{})



