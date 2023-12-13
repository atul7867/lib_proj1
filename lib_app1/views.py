from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,"home.html")

def all_emp(request):
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    print(emps) 
    return render(request,"all_emp.html",context)
def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,dept_id=dept,role_id=role,bonus=bonus,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return HttpResponse("employee add Successfully..")
    elif request.method=="GET":
        return render(request,"add_emp.html")
    else:
        return HttpResponse("some Error occurred in add_emp file,plz Try again..")

def remv_emp(request,emp_id=0):
    if emp_id:
        try:
            new_var=Employee.objects.get(id=emp_id)
            new_var.delete()
            return HttpResponse("employee remover successfully...")
        except:
            return HttpResponse("some error are occurred.. plz try again")
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    print(context)
    return render(request,"remv_emp.html",context)

def filter_emp(request):
    if request.method=="POST":
        name=request.POST['first_name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)  | Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)
        context={
            "emps":emps
        }
        return render(request,"all_emp.html",context)
    elif request.method=="GET":
        return render(request,"filter_emp.html")
    else:
        return HttpResponse("some error are occurred.plz try again..")