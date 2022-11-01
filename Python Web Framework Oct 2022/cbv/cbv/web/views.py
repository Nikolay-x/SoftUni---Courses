import random

from django import forms
from django.urls import reverse, reverse_lazy
# from django import views
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from cbv.web.models import Employee


# Create your views here.


def index(request):
    context = {
        'title': 'FBV',
    }

    # return HttpResponse('It works from FBV')

    return render(request, 'index.html', context)


# class IndexView:
#     def __init__(self):
#         self.values = [
#             random.randint(1, 15),
#         ]
#
#     @classmethod
#     def get_view(cls):
#         # instance = IndexView()
#         # the_view = instance.view
#         # print(the_view)
#         # return the_view
#
#         # return IndexView().view
#
#         return cls().view
#
#     def view(self, request):
#         return HttpResponse(f'It works! : {self.values}')
#
#
# Employee.objects.filter(pk=pk).get()
#
#
# class Index2View(IndexView):
#     def __init__(self):
#         super().__init__()
#         self.values.append(random.randint(15, 30))


def view(request):
    return HttpResponse('It works!')


# index()
# index_view = IndexView().get_view()


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Bare View',
        }

        # return HttpResponse('It works from CBV')

        return render(request, 'index.html', context)

    def post(self, request):
        pass

    # In Django Rest Framework
    # def put(self, request):
    #     pass


class IndexViewWithTemplate(views.TemplateView):
    template_name = 'index.html'
    extra_context = {'title': 'Template view'}  # Static context

    # Dynamic context
    def get_context_data(self, **kwargs):
        # Get "super"'s context
        context = super().get_context_data(**kwargs)

        # Add specific view stuff, one or more
        context['employees'] = Employee.objects.all()

        # Return the ready-to-use context
        return context


class IndexViewWithListView(views.ListView):
    context_object_name = 'employees'  # rename the built-in 'object_list' to 'employees'
    model = Employee

    # django by default is looking for web/employee_list.html,
    # if our template is different we need to specify it as per below
    template_name = 'index.html'

    extra_context = {'title': 'List view'}  # static context

    def get(self, *args, **kwargs):
        # put breakpoint on the below row to go around the code for better understanding
        return super().get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['pattern'] = self.__get_pattern()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(first_name__icontains=pattern)

        # queryset = queryset.order_by('first_name')

        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None


class EmployeeDetailsView(views.DetailView):
    context_object_name = 'employee'  # rename the built-in 'object' to 'employee'
    model = Employee
    template_name = 'employees/details.html'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                }
            ),
        }


class EmployeeCreateView(views.CreateView):
    template_name = 'employees/create.html'
    model = Employee
    fields = '__all__'
    # fields = ('first_name', 'last_name')
    # success_url = '/'  # static 'success_url'

    # dynamic 'success_url'
    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('employee details', kwargs={
            'pk': created_object.pk
        })

    # Replace authomatic form
    # form_class = EmployeeCreateForm

    # The below is dynamic way for form_class,
    # get form class based on certain conditions
    # def get_form_class(self):

    # Change the authomatic form
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class=form_class)
    #     for name, field in form.fields.items():
    #         field.widget.attrs['placeholder'] = 'Enter ' + ' '.join(name.split('_'))
    #
    #     return form


class EmployeeUpdateView(views.UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'employees/edit.html'

    # this is ok, because it gets the url when is needed,
    # by that time the urls are registered
    success_url = reverse_lazy('index')

    # will throw error, because 'reverse' is eager,
    # try to get the url before the url index is registered
    # success_url = reverse('index')

    # def get_success_url(self):
    #     created_object = self.object
    #     # return reverse('employee details', kwargs={
    #     return reverse_lazy('employee details', kwargs={
    #         'pk': created_object.pk
    #     })

    # 'dispatch' is the entry point to our view
    def dispatch(self, request, *args, **kwargs):
        # if the employee to update is the same as user logged in => continue
        return super().dispatch(request, *args, **kwargs)
        # else 401 authorized
