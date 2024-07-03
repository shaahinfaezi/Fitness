from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from bson.objectid import ObjectId
import pickle
from ai import track
from itertools import chain
import os
from pathlib import Path
# Create your views here.
id_=0

armid=0
backid=0
legid=0
shoulderid=0
chestid=0

AInum=2

dirname = os.path.dirname(__file__)
dirname=Path(dirname).parent.absolute().parent.absolute()
trainedAi= os.path.join(dirname, 'MLP_object')
trainedAi=trainedAi.replace('\\','/')


def index(request):
    print(trainedAi)
    return render(request,"index.html",{})
def free_workouts(request):
    return render(request,"free-workouts.html",{})
def arm(request):
    global armid
    numArm=0
    if Stats.count_documents({})==0:
        numArm=Workouts.count_documents({"Muscle_Group":"Arm"})-1
    else:
        numArm=AInum
    if request.method == "POST":
        if request.POST.get("next"):
            if(armid<numArm):
                armid+=1
        elif request.POST.get("prev"):
            if armid>0:
                armid-=1

    Arm_workouts=[]
    if Stats.count_documents({})==0:
        Arm_workouts=list(Workouts.find({"Muscle_Group":"Arm"}))
    else:
        restored_mlp = pickle.load(open(trainedAi, 'rb'))
        stats=list(Stats.find({}))
        stats=stats[0]
        Weight=float(stats["Current_Weight"])
        Age=float(stats["Age"])
        BMI=float(stats["BMI"])
        y_pred = restored_mlp.predict([[Weight,Age,BMI]])
         
        if y_pred<1:
            y_pred=1
        if y_pred>10:
            y_pred=10
        print(y_pred)  
        intensity=int(y_pred)
        Arm_workouts1=list(Workouts.find({"Muscle_Group":"Arm","intensity":f"{intensity}"}))
        if intensity>2:
            Arm_workouts2=list(Workouts.find({"Muscle_Group":"Arm","intensity":f"{intensity-1}"}))
            Arm_workouts3=list(Workouts.find({"Muscle_Group":"Arm","intensity":f"{intensity-2}"}))
        else:
            Arm_workouts2=list(Workouts.find({"Muscle_Group":"Arm","intensity":f"{intensity+1}"}))
            Arm_workouts3=list(Workouts.find({"Muscle_Group":"Arm","intensity":f"{intensity+2}"}))
        Arm_workouts=list(chain(Arm_workouts1,Arm_workouts2,Arm_workouts3))


    
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
    numChest=0
    if Stats.count_documents({})==0:
        numChest=Workouts.count_documents({trainedAi:"Chest"})-1
    else:
        numChest=AInum
    if request.method == "POST":
        if request.POST.get("next"):
            if(chestid<numChest):
                chestid+=1
        elif request.POST.get("prev"):
            if chestid>0:
                chestid-=1


    Chest_workouts=[]
    if Stats.count_documents({})==0:
        Chest_workouts=list(Workouts.find({"Muscle_Group":" Chest"}))
    else:
        restored_mlp = pickle.load(open(trainedAi, 'rb'))
        stats=list(Stats.find({}))
        stats=stats[0]
        Weight=float(stats["Current_Weight"])
        Age=float(stats["Age"])
        BMI=float(stats["BMI"])
        y_pred = restored_mlp.predict([[Weight,Age,BMI]])
        print(y_pred)   
        if y_pred<1:
            y_pred=1
        if y_pred>10:
            y_pred=10
        intensity=int(y_pred)
        Chest_workouts1=list(Workouts.find({"Muscle_Group":"Chest","intensity":f"{intensity}"}))
        if intensity>2:
            Chest_workouts2=list(Workouts.find({"Muscle_Group":"Chest","intensity":f"{intensity-1}"}))
            Chest_workouts3=list(Workouts.find({"Muscle_Group":"Chest","intensity":f"{intensity-2}"}))
        else:
            Chest_workouts2=list(Workouts.find({"Muscle_Group":"Chest","intensity":f"{intensity+1}"}))
            Chest_workouts3=list(Workouts.find({"Muscle_Group":"Chest","intensity":f"{intensity+2}"}))
        Chest_workouts=list(chain(Chest_workouts1,Chest_workouts2,Chest_workouts3))
    
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
    numBack=0
    if Stats.count_documents({})==0:
        numBack=Workouts.count_documents({"Muscle_Group":"Back"})-1
    else:
        numBack=AInum
    if request.method == "POST":
        if request.POST.get("next"):
            if(backid<numBack):
                backid+=1
        elif request.POST.get("prev"):
            if backid>0:
                backid-=1


    Back_workouts=[]
    if Stats.count_documents({})==0:
        Back_workouts=list(Workouts.find({"Muscle_Group":"Back"}))
    else:
        restored_mlp = pickle.load(open(trainedAi, 'rb'))
        stats=list(Stats.find({}))
        stats=stats[0]
        Weight=float(stats["Current_Weight"])
        Age=float(stats["Age"])
        BMI=float(stats["BMI"])
        y_pred = restored_mlp.predict([[Weight,Age,BMI]])
        print(y_pred)   
        if y_pred<1:
            y_pred=1
        if y_pred>10:
            y_pred=10
        intensity=int(y_pred)
        Back_workouts1=list(Workouts.find({"Muscle_Group":"Back","intensity":f"{intensity}"}))
        if intensity>2:
            Back_workouts2=list(Workouts.find({"Muscle_Group":"Back","intensity":f"{intensity-1}"}))
            Back_workouts3=list(Workouts.find({"Muscle_Group":"Back","intensity":f"{intensity-2}"}))
        else:
            Back_workouts2=list(Workouts.find({"Muscle_Group":"Back","intensity":f"{intensity+1}"}))
            Back_workouts3=list(Workouts.find({"Muscle_Group":"Back","intensity":f"{intensity+2}"}))
        Back_workouts=list(chain(Back_workouts1,Back_workouts2,Back_workouts3))
    
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
    numLeg=0
    if Stats.count_documents({})==0:
        numLeg=Workouts.count_documents({"Muscle_Group":"Leg"})-1
    else:
        numLeg=AInum
    if request.method == "POST":
        if request.POST.get("next"):
            if(legid<numLeg):
                legid+=1
        elif request.POST.get("prev"):
            if legid>0:
                legid-=1


    Leg_workouts=[]
    if Stats.count_documents({})==0:
        Leg_workouts=list(Workouts.find({"Muscle_Group":"Leg"}))
    else:
        restored_mlp = pickle.load(open(trainedAi, 'rb'))
        stats=list(Stats.find({}))
        stats=stats[0]
        Weight=float(stats["Current_Weight"])
        Age=float(stats["Age"])
        BMI=float(stats["BMI"])
        y_pred = restored_mlp.predict([[Weight,Age,BMI]])
        print(y_pred)  
        if y_pred<1:
            y_pred=1
        if y_pred>10:
            y_pred=10 
        intensity=int(y_pred)
        Leg_workouts1=list(Workouts.find({"Muscle_Group":"Leg","intensity":f"{intensity}"}))
        if intensity>2:
            Leg_workouts2=list(Workouts.find({"Muscle_Group":"Leg","intensity":f"{intensity-1}"}))
            Leg_workouts3=list(Workouts.find({"Muscle_Group":"Leg","intensity":f"{intensity-2}"}))
        else:
            Leg_workouts2=list(Workouts.find({"Muscle_Group":"Leg","intensity":f"{intensity+1}"}))
            Leg_workouts3=list(Workouts.find({"Muscle_Group":"Leg","intensity":f"{intensity+2}"}))
        Leg_workouts=list(chain(Leg_workouts1,Leg_workouts2,Leg_workouts3))
    
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
    numShoulder=0
    if Stats.count_documents({})==0:
        numShoulder=Workouts.count_documents({"Muscle_Group":"Shoulder"})-1
    else:
        numShoulder=AInum
    if request.method == "POST":
        if request.POST.get("next"):
            if(shoulderid<numShoulder):
                shoulderid+=1
        elif request.POST.get("prev"):
            if shoulderid>0:
                shoulderid-=1


    Shoulder_workouts=[]
    if Stats.count_documents({})==0:
        Shoulder_workouts=list(Workouts.find({"Muscle_Group":"Shoulder"}))
    else:
        restored_mlp = pickle.load(open(trainedAi, 'rb'))
        stats=list(Stats.find({}))
        stats=stats[0]
        Weight=float(stats["Current_Weight"])
        Age=float(stats["Age"])
        BMI=float(stats["BMI"])
        y_pred = restored_mlp.predict([[Weight,Age,BMI]])
        print(y_pred)   

        if y_pred<1:
            y_pred=1
        if y_pred>10:
            y_pred=10
        intensity=int(y_pred)
        Shoulder_workouts1=list(Workouts.find({"Muscle_Group":"Shoulder","intensity":f"{intensity}"}))
        if intensity>2:
            Shoulder_workouts2=list(Workouts.find({"Muscle_Group":"Shoulder","intensity":f"{intensity-1}"}))
            Shoulder_workouts3=list(Workouts.find({"Muscle_Group":"Shoulder","intensity":f"{intensity-2}"}))
        else:
            Shoulder_workouts2=list(Workouts.find({"Muscle_Group":"Shoulder","intensity":f"{intensity+1}"}))
            Shoulder_workouts3=list(Workouts.find({"Muscle_Group":"Shoulder","intensity":f"{intensity+2}"}))
        Shoulder_workouts=list(chain(Shoulder_workouts1,Shoulder_workouts2,Shoulder_workouts3))
    
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
        bmi=request.POST.get("BMI")
        Current_bench_PR=request.POST.get("Current_bench_PR")
        Bench_PR_Goal=request.POST.get("Bench_PR_Goal")
        Current_squat_PR=request.POST.get("Current_squat_PR")
        Squat_PR_Goal=request.POST.get("Squat_PR_Goal")
        Current_deadlift_PR=request.POST.get("Current_deadlift_PR")
        Deadlift_PR_Goal=request.POST.get("Deadlift_PR_Goal")
        dic={"Age":Age,
             "Current_Weight":Current_Weight,
             "Goal_Weight":Goal_Weight,
             "BMI":bmi,
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
        
        if Workout_Plan.count_documents({"Year":Year,"Month":Month,"Day":Day})==0:
            Workout_Plan.insert_one(dic)
        else:
            cursor=Workout_Plan.find_one({"Year":Year,"Month":Month,"Day":Day})
            idd=cursor["_id"]
            Workout_Plan.replace_one({"_id":idd},dic)
    return render(request,"contact.html",{})



