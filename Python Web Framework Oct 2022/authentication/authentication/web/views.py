from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic as views

# Create your views here.

from django.contrib.auth.models import User

from authentication.web.decorators import allow_groups


# Require 'login' in function based views
@login_required(login_url='/login/')  # not desirable to define the login url here, the proper way is in settings
def show_profile(request):
    return HttpResponse(f'You are {request.user}')


# Require 'login' in class based views
class ProfileView(auth_mixins.LoginRequiredMixin, views.View):
    # @method_decorator(login_required())  # this is also a way but not the preferred one
    def get(self, request):
        return HttpResponse(f'You are {self.request.user.username}')


# @allow_groups
@allow_groups(groups=['Users_statistics'])
def index(request):
    print(request.user)
    print(
        authenticate(username='nb', password='password'),
        authenticate(username='minkov', password='D0nch0!%123'),
        authenticate(username='minkov', password='D0123nch0!%123'),  # not valid credentials
        authenticate(username='donchominkov', password='d0nc40mink0v'),
    )

    # new_user = User.objects.create_user(
    #     username='donchominkov',
    #     password='d0nc40mink0v',
    #     first_name='Doncho',
    #     last_name='Minkov',
    # )
    user_message = '' if request.user.is_authenticated else ' not '
    return HttpResponse(f'The user is {user_message}authenticated')


def permissions_debug(request):
    usernames = (
        'nb',  # superuser
        'minkov',  # User with Group...
        'donchominkov',
        # 'Pesho'
    )

    users = User.objects.filter(username__in=usernames)
    permissions_to_check = (
        'auth.add.user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user',
    )

    for user in users:
        print('-' * 30)
        print(f'User={user}')

        # User must have all the permissions from 'permissions_to_check'
        print(f'{permissions_to_check}: {user.has_perms(permissions_to_check)}')

        # User must have any permission from 'permissions_to_check'
        for perm in permissions_to_check:
            print(f'{perm}: {user.has_perm(perm)}')

        # Dont't do this, it's wrong
        print(user.user_permissions.all())
        print('-' * 30)

    print(users)
    return HttpResponse('It works')


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Pesho',
        password='User.objects.create_',
    )

    # Handles the following:
    # - creates the session
    # - attaches 'user' to request
    login(request, user)
    print(request.user)
    return HttpResponse('It works')


'''
Ways to create users:
1. 'python manage.py createsuperuser'
2. From Django Admin by superuser
3. With code:
    - 'User.objects.create.user()'
    - 'User.objects.create_superuser()'
'''

'''
minkov
D0nch0!%123
'''