from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Student
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def nine(request):
    context= {'course':'python',
              'duration': 2,
              'error':'Invalid login details',
              'students':['Abi','Bins','Chris']
              }
    return render(request,'home.html',context)

def eight(request):
    lis=[1,2,3,5,7]
    for i in lis:
        if i % 2 == 0:
            res = "List contains even numbers"
            break
        else:
            res = "List doesnot contain even numbers"


    return HttpResponse(res)

# def ten(request):
#     stud = Student(name='Swathi',place='TVM',address='KKK',email='swathi@hgsd.com',phone='467899008')
#     stud.save()
#     return HttpResponse('Data saved to model')

def formview(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        place= request.POST.get('place')
        address= request.POST.get("address")
        email= request.POST.get("email")
        phone= request.POST.get('phone')
        stud= Student(name=name,place=place,address=address,email=email,phone=phone)
        stud.save()
        return HttpResponse('Saved successfully')
    return render(request,'form.html',{})


def viewdata(request):
    students = Student.objects.all()
    return render(request,'viewdata.html',{'students':students})

def index(request):
    return render(request,'3.html',{})

def twelve(request):
    stud = Student.objects.filter(address = 'RRR')
    return render(request,'viewdata.html',{'students':stud})


def usercreate(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.__dict__)
        return HttpResponse('Data saved for %s' %form.cleaned_data['username'])
    return render(request,'form_template.html',{'form':form})