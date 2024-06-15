from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from bson.objectid import ObjectId
# Create your views here.
id_=0

armid=0
backid=0
legid=0
shoulderid=0
chestid=0

def index(request):
    return render(request,"index.html",{})
def free_workouts(request):
    return render(request,"free-workouts.html",{})
def arm(request):
    global armid
    if request.method == "POST":
        if request.POST.get("next"):
            if(armid<Workouts.count_documents({"Muscle_Group":"Arm"})-1):
                armid+=1
        elif request.POST.get("prev"):
            if armid>0:
                armid-=1


    Arm_workouts=list(Workouts.find({"Muscle_Group":"Arm"}))
    
    name1=Arm_workouts[armid]["Name1"]

    name2=Arm_workouts[armid]["Name2"]

    name3=Arm_workouts[armid]["Name3"]

    name4=Arm_workouts[armid]["Name4"]

    name5=Arm_workouts[armid]["Name5"]

    sets1=Arm_workouts[armid]["Sets1"]

    sets2=Arm_workouts[armid]["Sets2"]

    sets3=Arm_workouts[armid]["Sets3"]

    sets4=Arm_workouts[armid]["Sets4"]

    sets5=Arm_workouts[armid]["Sets5"]
    

    dic={
        "w1":f"{name1} {sets1}",
        "w2":f"{name2} {sets2}",
        "w3":f"{name3} {sets3}",
        "w4":f"{name4} {sets4}",
        "w5":f"{name5} {sets5}",
             }

    return render(request,"arm.html",dic)
def chest(request):
    global chestid
    if request.method == "POST":
        if request.POST.get("next"):
            if(chestid<Workouts.count_documents({"Muscle_Group":"Chest"})-1):
                chestid+=1
        elif request.POST.get("prev"):
            if chestid>0:
                chestid-=1


    Chest_workouts=list(Workouts.find({"Muscle_Group":"Chest"}))
    
    name1=Chest_workouts[chestid]["Name1"]

    name2=Chest_workouts[chestid]["Name2"]

    name3=Chest_workouts[chestid]["Name3"]

    name4=Chest_workouts[chestid]["Name4"]

    name5=Chest_workouts[chestid]["Name5"]

    sets1=Chest_workouts[chestid]["Sets1"]

    sets2=Chest_workouts[chestid]["Sets2"]

    sets3=Chest_workouts[chestid]["Sets3"]

    sets4=Chest_workouts[chestid]["Sets4"]

    sets5=Chest_workouts[chestid]["Sets5"]
    

    dic={
        "w1":f"{name1} {sets1}",
        "w2":f"{name2} {sets2}",
        "w3":f"{name3} {sets3}",
        "w4":f"{name4} {sets4}",
        "w5":f"{name5} {sets5}",
             }

    return render(request,"chest.html",dic)
def back(request):
    global backid
    if request.method == "POST":
        if request.POST.get("next"):
            if(backid<Workouts.count_documents({"Muscle_Group":"Back"})-1):
                backid+=1
        elif request.POST.get("prev"):
            if backid>0:
                backid-=1


    Back_workouts=list(Workouts.find({"Muscle_Group":"Back"}))
    
    name1=Back_workouts[backid]["Name1"]

    name2=Back_workouts[backid]["Name2"]

    name3=Back_workouts[backid]["Name3"]

    name4=Back_workouts[backid]["Name4"]

    name5=Back_workouts[backid]["Name5"]

    sets1=Back_workouts[backid]["Sets1"]

    sets2=Back_workouts[backid]["Sets2"]

    sets3=Back_workouts[backid]["Sets3"]

    sets4=Back_workouts[backid]["Sets4"]

    sets5=Back_workouts[backid]["Sets5"]
    

    dic={
        "w1":f"{name1} {sets1}",
        "w2":f"{name2} {sets2}",
        "w3":f"{name3} {sets3}",
        "w4":f"{name4} {sets4}",
        "w5":f"{name5} {sets5}",
             }

    return render(request,"back.html",dic)
def leg(request):
    global legid
    if request.method == "POST":
        if request.POST.get("next"):
            if(legid<Workouts.count_documents({"Muscle_Group":"Leg"})-1):
                legid+=1
        elif request.POST.get("prev"):
            if legid>0:
                legid-=1


    Leg_workouts=list(Workouts.find({"Muscle_Group":"Leg"}))
    
    name1=Leg_workouts[legid]["Name1"]

    name2=Leg_workouts[legid]["Name2"]

    name3=Leg_workouts[legid]["Name3"]

    name4=Leg_workouts[legid]["Name4"]

    name5=Leg_workouts[legid]["Name5"]

    sets1=Leg_workouts[legid]["Sets1"]

    sets2=Leg_workouts[legid]["Sets2"]

    sets3=Leg_workouts[legid]["Sets3"]

    sets4=Leg_workouts[legid]["Sets4"]

    sets5=Leg_workouts[legid]["Sets5"]
    

    dic={
        "w1":f"{name1} {sets1}",
        "w2":f"{name2} {sets2}",
        "w3":f"{name3} {sets3}",
        "w4":f"{name4} {sets4}",
        "w5":f"{name5} {sets5}",
             }

    return render(request,"leg.html",dic)
def shoulder(request):
    global shoulderid
    if request.method == "POST":
        if request.POST.get("next"):
            if(shoulderid<Workouts.count_documents({"Muscle_Group":"Shoulder"})-1):
                shoulderid+=1
        elif request.POST.get("prev"):
            if shoulderid>0:
                shoulderid-=1


    Shoulder_workouts=list(Workouts.find({"Muscle_Group":"Shoulder"}))
    
    name1=Shoulder_workouts[shoulderid]["Name1"]

    name2=Shoulder_workouts[shoulderid]["Name2"]

    name3=Shoulder_workouts[shoulderid]["Name3"]

    name4=Shoulder_workouts[shoulderid]["Name4"]

    name5=Shoulder_workouts[shoulderid]["Name5"]

    sets1=Shoulder_workouts[shoulderid]["Sets1"]

    sets2=Shoulder_workouts[shoulderid]["Sets2"]

    sets3=Shoulder_workouts[shoulderid]["Sets3"]

    sets4=Shoulder_workouts[shoulderid]["Sets4"]

    sets5=Shoulder_workouts[shoulderid]["Sets5"]
    

    dic={
        "w1":f"{name1} {sets1}",
        "w2":f"{name2} {sets2}",
        "w3":f"{name3} {sets3}",
        "w4":f"{name4} {sets4}",
        "w5":f"{name5} {sets5}",
             }

    return render(request,"shoulder.html",dic)
def shop(request):
    global id_
    if request.method == "POST":
        if request.POST.get("next"):
            if(id_<Workout_Plan.count_documents({})-1):
                id_+=1
        elif request.POST.get("prev"):
            if id_>0:
                id_-=1

    if Stats.count_documents({})==0 :
        Goal_Weight="0 KG"
        Current_Weight="0 KG"
        Squat_PR_Goal="0 KG"
        Current_squat_PR="0 KG"
        Bench_PR_Goal="0 KG"
        Current_bench_PR="0 KG"
        Deadlift_PR_Goal="0 KG"
        Current_deadlift_PR="0 KG"
    else:
    
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

    if Workout_Plan.count_documents({})==0:
        Muscle_group="Go to the gym!"
        Date="0/0/0"
        Description=""
    else:

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



