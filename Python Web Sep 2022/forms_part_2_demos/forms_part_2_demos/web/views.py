from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_part_2_demos.web.forms import TodoForm, TodoCreateForm, PersonCreateForm
from forms_part_2_demos.web.models import Person


# # # View for TodoForm - form
# def index(request):
#     if request.method == 'GET':
#         form = TodoForm()
#     else:
#         form = TodoForm(request.POST)
#
#         if form.is_valid():
#             return HttpResponse('All is valid')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'index.html', context)


# # View for TodoCreateForm - model form
# def index(request):
#     if request.method == 'GET':
#         form = TodoCreateForm()
#     else:
#         form = TodoCreateForm(request.POST)
#
#         if form.is_valid():
#             # model = form.instance
#             # model.full_clean()
#             form.save()
#             return HttpResponse('All is valid')
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'index.html', context)


# View demo to show how to override errors
def index(request):
    form_class = TodoForm

    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)

        if form.is_valid():
            # form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-persons.html', context)


def create_person(request):
    if request == 'GET':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list persons')

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context)
