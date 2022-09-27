from random import choice

from django.http import HttpResponse, HttpRequest, HttpResponseNotFound, HttpResponseBadRequest, Http404
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.


# # Without render
# def show_departments(request: HttpRequest, *args, **kwargs):
#     print(request.method)
#     print(request.GET)  # query params (?param1:value1&param2:value2)
#     print(request.POST)  # body of HTTP request
#     print(request.get_port())
#     print(request.get_host())
#     print(request.headers)
#
#     order_by = request.GET.get('order_by', 'name')
#     body = f'path: {request.path}, args={args}, kwargs={kwargs}, order_by: {order_by}'
#     return HttpResponse(body)


def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        'page_title': 'Departments',
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name')
    }

    return render(request, 'departments/all.html', context)


def show_department_details(request: HttpRequest, department_id):
    body = f'path: {request.path}, id: {department_id}'
    return HttpResponse(body)


def redirect_to_first_department(request):
    possible_order_by = ['name', 'age', 'id']
    order_by = choice(possible_order_by)
    # to = 'https://softuni.bg'
    # to = f'/departments/?order_by={order_by}'
    # return redirect('show departments')
    return redirect('show department details', department_id=13)


def show_not_found(request):
    # status_code = 404
    # if status_code == 404:
    #     return HttpResponseNotFound('This is not found')
    # elif status_code == 400:
    #     return HttpResponseBadRequest('This is bad request')

    # status_code = 400
    # return HttpResponse('Error', status=status_code)

    # print('With response')

    # get_object_or_404(Task)
    # raise Http404('Not found')

    return HttpResponseNotFound('This is not found')

    # values = []
    # return HttpResponse(values[0])
