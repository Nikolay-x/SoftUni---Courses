from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model

from petstagram.accounts.forms import UserCreateForm
from petstagram.photos.models import Photo

# Create your views here.


# Always get the 'user model' with 'get_user_model'
UserModel = get_user_model()


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        context['pets_count'] = self.object.pet_set.count()

        # Photo.objects.get().photolike_set

        # N+1 query problem, the below code makes N+1 db requests
        # photos = self.object.photo_set.all()

        # N+1 query problem, the below code makes 2 db requests
        photos = self.object.photo_set\
            .prefetch_related('photolike_set')
        # .select_related('user')  # two functions in series

        Photo.objects.select_related()
        # Photo.objects.prefetch_related()

        context['photos_count'] = photos.count()
        context['likes_count'] = sum(x.photolike_set.count() for x in photos)

        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email',)

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
