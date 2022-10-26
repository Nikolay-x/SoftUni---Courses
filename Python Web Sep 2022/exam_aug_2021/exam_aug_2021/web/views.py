from django.shortcuts import render, redirect

from exam_aug_2021.web.forms import ProfileCreateForm, AddBookForm, EditBookForm, ProfileEditForm, ProfileDeleteForm
from exam_aug_2021.web.models import Profile, Book


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    profile = get_profile()

    if profile is None:
        return add_profile(request)

    context = {
        'books': Book.objects.all(),
        'profile': profile,
    }

    return render(request, 'home-with-profile.html', context)


def add_profile(request):
    if get_profile() is not None:
        return redirect('home page')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'hide_nav_links': True,
    }

    return render(request, 'home-no-profile.html', context)


def add_book(request):
    profile = get_profile()
    if request.method == 'GET':
        form = AddBookForm()
    else:
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add-book.html', context)


def edit_book(request, book_id):
    book = Book.objects.filter(pk=book_id).get()
    profile = get_profile()

    if request.method == 'GET':
        form = EditBookForm(instance=book)
    else:
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'book_id': book_id,
        'profile': profile,
    }

    return render(request, template_name='edit-book.html', context=context)


def book_details(request, book_id):
    book = Book.objects.filter(pk=book_id).get()
    profile = get_profile()

    context = {
        'book': book,
        'book_id': book_id,
        'profile': profile,
    }

    return render(request, 'book-details.html', context)


def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('home page')


def profile_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    books = Book.objects.all()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)

    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        profile.delete()
        books.delete()
        return redirect('home page')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)
