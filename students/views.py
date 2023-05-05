from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .form import MyForm
from .models import Student

# Create your views here.



def home_page(request,*args,**kwargs):
    myform=MyForm(request.POST or None)
    if myform.is_valid():
        myform.save()
        myform=MyForm()
    
    context={
        "HTMLFORM":myform
    }
    return render(request,"index.html",context)




def see_post(request, *args ,**kwargs):
    odj=Student.objects.all().order_by('level')[:5]
    content_post={
        'objects':odj
    }

    return render(request, 'post.html',content_post)


def delete_view(request, id):
    
    odj=Student.objects.get(pk=id)
    if request.method == 'POST':
        odj.delete()
        return HttpResponseRedirect('../../')



def update_view(request,id):
    myform=MyForm()
    if request.method == 'POST':
        obj= Student.objects.get(pk=id)
        myform=MyForm(request.POST , instance=obj)
        if myform.is_valid():
            obj.save()
            
        

    context={
        "HTMLFORM":myform
        
    }
    return render(request, 'update.html',context)
