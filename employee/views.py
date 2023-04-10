from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from employee.models import Employee
from employee.forms import EmployeeForm

def index(request):
    employees = Employee.objects.all()
    return render(request, 'employee/index.html', {'employees': employees})

def show(request, id):
    employee = get_object_or_404(Employee,id=id)
    return render(request, 'employee/show.html', {'employee': employee})

def create(request):
    if request.method == 'POST': 
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("employees:index"))
        else:
            errors = form.errors.values
            messages.info(request, "Failed to Save!") 
            context = { 'form': form, 'errors': errors }
            return render(request, 'employee/create.html', context)
    else:
        form = EmployeeForm()
    return render(request, 'employee/create.html', {'form': form})

def update(request, id):
    employee = get_object_or_404(Employee,id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,  instance=employee)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("employees:show", args=(id,)))
        else:
            errors = form.errors.values
            messages.info(request, "Failed to Update!")
            context = { 'employee': employee, 'form': form, 'errors': errors }
            return render(request, 'employee/update.html', context)
    else:
        form = EmployeeForm(instance=employee)
        context = { 'form': form, 'employee': employee }
    return render(request, 'employee/update.html', context)

def destroy(request, id):
    employee = get_object_or_404(Employee,id=id)
    employee.delete()
    return HttpResponseRedirect(reverse("employees:index"))

