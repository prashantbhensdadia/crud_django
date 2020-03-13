from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm


# Create your views here.

def create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/get')

    else:
        form = EmployeeForm()
    return render(request, 'crud_app/index.html', {'form':form})


def show(request):
    employees = Employee.objects.all()
    return render(request, 'crud_app/show.html', {'employees':employees})



def update(request, id):
    employee = Employee.objects.get(id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES, instance = employee)
        if form.is_valid():
            form.save()
            return redirect("/get")
    else:
        form = EmployeeForm(instance = employee)
    return render(request, 'crud_app/edit.html', {'form':form})



def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/get")