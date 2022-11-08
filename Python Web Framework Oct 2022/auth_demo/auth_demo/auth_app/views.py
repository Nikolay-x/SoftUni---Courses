from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.views import generic as views

from auth_demo.auth_app.forms import SignUpForm

# Create your views here.


def to_delete(request):
    # User
    # UserCreationForm
    pass


class SignUpView(views.CreateView):
    template_name = 'auth/sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    # Signs the user in after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)

        return result


# class SignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#
#
# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # user = authenticate(request, username=username, password=password)
#             user = authenticate(request, **form.cleaned_data)
#             # print(user)
#
#             if user:
#                 login(request, user)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context)


class SignInView(auth_views.LoginView):
    template_name = 'auth/sign-in.html'
    success_url = reverse_lazy('index')

    # def get_success_url(self):
    #     if self.success_url:
    #         return self.success_url
    #
    #     return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_views.LogoutView):
    template_name = 'auth/sign-out.html'


'''
B0nev%123
'''

'''
pre_clean
clean
post_clean
'''
