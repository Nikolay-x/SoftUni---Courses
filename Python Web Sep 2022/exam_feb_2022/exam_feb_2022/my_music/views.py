from django.shortcuts import render, redirect

from exam_feb_2022.my_music.forms import ProfileCreateForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from exam_feb_2022.my_music.models import Profile, Album


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
        'albums': Album.objects.all(),
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


def add_album(request):
    if request.method == 'GET':
        form = AddAlbumForm()
    else:
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, template_name='add-album.html', context=context)


def album_details(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    context = {
        'album': album,
        'album_id': album_id,
    }

    return render(request, 'album-details.html', context)


def edit_album(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    if request.method == 'GET':
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album_id': album_id,
    }

    return render(request, template_name='edit-album.html', context=context)


def delete_album(request, album_id):
    album = Album.objects.filter(pk=album_id).get()

    if request.method == 'GET':
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        album.delete()
        return redirect('home page')

    context = {
        'form': form,
        'album': album,
        'album_id': album_id,
    }

    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count,
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    albums = Album.objects.all()

    if request.method == 'POST':
        profile.delete()
        albums.delete()
        return redirect('home page')

    return render(request, 'profile-delete.html')
