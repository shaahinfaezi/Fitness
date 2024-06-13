from django import forms

class LogWorkout(forms.Form):
    Muscle_Group=forms.CharField(label="Muscle Group",max_length=256)
    Year=forms.DateField()