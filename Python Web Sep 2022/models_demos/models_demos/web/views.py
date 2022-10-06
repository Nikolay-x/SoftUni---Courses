from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from models_demos.web.models import Employee, Department, Project


# Create your views here.


def index(request):
    # employees = Employee.objects.all()
    # here 'employees' is not executed QuerySet, we can do additional operations on it
    # employees_list = list(employees)
    # print(list(User.objects.all()))
    # print(list(Department.objects.all()))
    # print(employees_list)
    # print(employees)

    # in this case the DB return all results, we filter them manually with code,
    # all DB objects go to computer RAM.
    employees = [e for e in Employee.objects.all() if e.department_id == 6]

    # here DB return only the filter results, like this only the needed DB objects
    # go to computer RAM, this is the preferred way.
    # employees2 = Employee.objects.filter(department_id=2)\
    employees2 = Employee.objects\
        .filter(department__name='Engineering')\
        .order_by('last_name', 'first_name')
    # 'department__name' in filter is like 'department.name'

    # 'get' returns an object, not QuerySet
    # 'get' returns a single object and throws when none or multiple results
    department = Department.objects.get(pk=6)

    # 'get' is not lazy method, it is eager
    # # print(Employee.objects.get(level=Employee.LEVEL_SENIOR))
    # Employee.objects.get(level=Employee.LEVEL_JUNIOR)

    # print(department)

    # get_object_or_404(Employee, level=Employee.LEVEL_JUNIOR)

    Employee.objects.filter(level=Employee.LEVEL_REGULAR)\
        .first()

    context = {
        'employees': employees,
        'employees2': employees2,
        'department': department,
    }

    return render(request, 'index.html', context)


def department_details(request, pk, slug):
    context = {
        'department': get_object_or_404(Department, pk=pk, slug=slug)
    }
    return render(request, 'department_details.html', context)


def delete_employee(request, pk):
    department_pk = 6

    # When 'RESTRICTED' this must be done explicitly
    # When 'CASCADE' this is done implicitly
    Employee.objects.filter(department_id=department_pk)\
        .delete()
    get_object_or_404(Department, pk=department_pk)\
        .delete()

    # employee = get_object_or_404(Employee, pk=pk)
    # employee.delete()
    #
    # # Deletes all projects with this criteria
    # Project.objects.filter()\
    #     .delete()
    #
    # # Deletes all projects
    # Project.objects.all()\
    #     .delete()

    return redirect('index')
