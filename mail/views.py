from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login as lg,logout,authenticate
from django.core.mail import send_mail
from .models import Employees
from django.contrib.auth.decorators import login_required
def login(request):
    if request.method=='POST':
        user = authenticate(username=request.POST.get('name'),
                            password=request.POST.get('Password1'))
        if user:
            lg(request,user)
            return redirect('index')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        Employees.objects.create(created_by=User.objects.first(),
                                 first_name=request.POST.get("firstname"),
                                 last_name=request.POST.get("lastname"),
                                 email=request.POST.get("email"),
                                 phone=request.POST.get("phone"),
                                 password1=request.POST.get("password1"),
                                 password2=request.POST.get("password2")
                                 )
        return render(request,'login.html')
    return render(request,'signup.html')


@login_required(login_url='emp')
def emp(request):
    employee=Employees.objects.all()
    context={'emp':employee}
    return render(request,'index.html',context)
@login_required(login_url='contact')
def contact(request,id):
    employee=Employees.objects.filter(pk=id)
    emai=[emp.email for emp in employee]
    print(emai,request.user)
    if request.method=='POST':
        subject=request.POST.get('subject')
        msg=request.POST.get('message')
        send_mail(
            subject,
            msg,
            'testerdjango6@gmail.com',
            [*emai,],
            fail_silently=False,
        )
        return render(request,'contact.html',{'data':employee,'msg':"we send your message now"})
    print(employee)
    return render(request,'contact.html',{'data':employee})

def log_out(request):
    logout(request)
    return redirect('login')

