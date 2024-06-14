from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from bson.objectid import ObjectId
# Create your views here.
id_=0

def index(request):
    return render(request,"index.html",{})
def shop(request):

    if request.method == "POST":
        if request.POST.get("next"):
            if(id_<Workout_Plan.count_documents({})-1):
                id_+=1
        elif request.POST.get("prev"):
            if id_>0:
                id_-=1


    stats=list(Stats.find({}))
    stats=stats[0]
    Goal_Weight=stats["Goal_Weight"]
    Current_Weight=stats["Current_Weight"]
    Squat_PR_Goal=stats["Squat_PR_Goal"]
    Current_squat_PR=stats["Current_squat_PR"]
    Bench_PR_Goal=stats["Bench_PR_Goal"]
    Current_bench_PR=stats["Current_bench_PR"]
    Deadlift_PR_Goal=stats["Deadlift_PR_Goal"]
    Current_deadlift_PR=stats["Current_deadlift_PR"]

    workouts=Workout_Plan.find().sort( { "Year": 1, "Month": 1 ,"Day": 1} )
    workouts=list(workouts)

    Muscle_group=workouts[id_]["Muscle_group"]
    Year=workouts[id_]["Year"]
    Month=workouts[id_]["Month"]
    Day=workouts[id_]["Day"]
    Date=f"{Month}/{Day}/{Year}"
    Description=workouts[id_]["Description"]
    

    dic={
             "Current_Weight":Current_Weight,
             "Goal_Weight":Goal_Weight,
             "Current_bench_PR":Current_bench_PR,
             "Bench_PR_Goal":Bench_PR_Goal,
             "Current_squat_PR":Current_squat_PR,
             "Squat_PR_Goal":Squat_PR_Goal,
             "Current_deadlift_PR":Current_deadlift_PR,
             "Deadlift_PR_Goal":Deadlift_PR_Goal,
             "Muscle_group":Muscle_group,
             "Date":Date,
             "Description":Description
             }

    return render(request,"shop.html",dic)
def blog(request):
    if request.method == "POST":
        Age=request.POST.get("name")
        Current_Weight=request.POST.get("Current_Weight")
        Goal_Weight=request.POST.get("Goal_Weight")
        Height=request.POST.get("Height")
        Current_bench_PR=request.POST.get("Current_bench_PR")
        Bench_PR_Goal=request.POST.get("Bench_PR_Goal")
        Current_squat_PR=request.POST.get("Current_squat_PR")
        Squat_PR_Goal=request.POST.get("Squat_PR_Goal")
        Current_deadlift_PR=request.POST.get("Current_deadlift_PR")
        Deadlift_PR_Goal=request.POST.get("Deadlift_PR_Goal")
        dic={"Age":Age,
             "Current_Weight":Current_Weight,
             "Goal_Weight":Goal_Weight,
             "Height":Height,
             "Current_bench_PR":Current_bench_PR,
             "Bench_PR_Goal":Bench_PR_Goal,
             "Current_squat_PR":Current_squat_PR,
             "Squat_PR_Goal":Squat_PR_Goal,
             "Current_deadlift_PR":Current_deadlift_PR,
             "Deadlift_PR_Goal":Deadlift_PR_Goal,
             }
        if Stats.count_documents({})==0:
            Stats.insert_one(dic)
        else:   
            obid=[str(id) for id in Stats.distinct('_id')]
            _id=ObjectId(obid[0])
            Stats.replace_one({"_id":_id},dic)
    return render(request,"blog.html",{})
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



