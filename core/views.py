from django.shortcuts import render,HttpResponseRedirect
from .forms import  StudentRegistation
from .models import User

# Create your views here.
def add_show(request):
    if request.method=="POST":
        fm=StudentRegistation(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            fm=StudentRegistation()
    else:
        fm=StudentRegistation()
    studata=User.objects.all()
    return render(request,'core/addshow.html',{'form':fm,'stu':studata})





def update_data(request,id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistation(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistation(instance=pi)
    return render(request,'core/update.html',{"form":fm})

    



def delete_data(request,id):
    if request.method =="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')



