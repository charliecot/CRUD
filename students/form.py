from django import forms
from .models import Student
 

class MyForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control form-control-lg' ,'placeholder':'your name...'}),
            'gender': forms.Select(choices=[ ('male','MALE'),('female','FEMALE') ],attrs={'class':'form-control form-control-lg','placeholder':'your gender'}),
            'matricule': forms.TextInput(attrs={'class':'form-control form-control-lg','placeholder':'your matricule number'}),
            'level': forms.Select(choices=[(200,200),(300,300),(400,400)],attrs={'class':'form-control form-control-lg'})
            
        }

        labels={
            'name':"",
            'gender':"",
            'matricule':"",
            'level':""
        }



  
