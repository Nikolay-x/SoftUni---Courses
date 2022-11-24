from django.contrib import admin

from drf_demos.api.models import Employee, Department


# Register your models here.


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


'''

REST => Representational State Transfer

Django App: 

# Models:
Employees
Department

Operations:
POST: api/employees:
JSON:
{
    'name': 'Doncho',
    'salary': 1000,
    'department_id': 1,
}

GET
PUT
DELETE

RestAPI:

- All books or filtered, or paged:
GET /api/books/
GET /api/books?category=sci_fi
GET /api/books?page=1
GET /api/books?page=1&category=sci_fi

- Book details:
GET /api/books/1

- Create book:
POST /api/books with {body}

- Update book:
PUT /api/books/1 with {body}

- Delete book:
Delete /api/books/1

POST /api/books
GET /api/books

GET     /api/books/1
PUT     /api/books/1
DELETE  /api/books/1

'''
