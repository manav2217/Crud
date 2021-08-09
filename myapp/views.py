from django.shortcuts import render,redirect
from .models import Employee
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == "POST":
        ename = request.POST['en']
        eemail = request.POST['em']
        emobile = request.POST['mobo']
        eid = request.POST['eid']
        
        exist_user = Employee.objects.filter(eemail=eemail).first()
        if exist_user:
            message = "User already exist"
            return render(request , "index.html" , {'msg':message})
        new_user = Employee.objects.create(
            ename = ename,
            eemail = eemail,
            emob = emobile,
            eid = eid, 
        )
        new_user.save()
        return redirect("show")
    return render(request , "index.html")

def show(request):
    employee = Employee.objects.all()
    return render(request , "show.html" , {"employees":employee})

def edit(request,pk):
    edit_user = Employee.objects.get(id=pk)
    return render(request , "edit.html" , {"exit_user":edit_user})

def edit_user(request,pk):
    edit_details = Employee.objects.get(id=pk)
    edit_details.ename = request.POST['en']
    edit_details.eemail = request.POST['em']
    edit_details.emob = request.POST['mobo']
    edit_details.eid = request.POST['eid']
    edit_details.save()
    return redirect("show")

def delete_user(request,pk):
    exit_user = Employee.objects.get(id=pk)
    exit_user.delete()
    return redirect("show") 