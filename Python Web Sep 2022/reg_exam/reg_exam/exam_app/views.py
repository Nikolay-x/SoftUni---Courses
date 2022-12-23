from django.shortcuts import render, redirect

from reg_exam.exam_app.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm
from reg_exam.exam_app.models import Profile, Car


# Create your views here.


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def home_page(request):
    profile = get_profile()

    context = {
        'profile': profile,
    }

    return render(request, 'index.html', context)


def profile_create(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def catalogue(request):
    cars = Car.objects.all()
    cars_count = Car.objects.count()

    context = {
        'cars': cars,
        'cars_count': cars_count,
    }

    return render(request, 'catalogue.html', context)


def car_create(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'car-create.html', context)


def car_details(request, car_id):
    car = Car.objects.filter(pk=car_id).get()

    context = {
        'car': car,
        'car_id': car_id,
    }

    return render(request, 'car-details.html', context)


class EditAlbumForm:
    pass


def car_edit(request, car_id):
    car = Car.objects.filter(pk=car_id).get()

    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'car_id': car_id,
    }

    return render(request, 'car-edit.html', context)


def car_delete(request, car_id):
    car = Car.objects.filter(pk=car_id).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        car.delete()
        return redirect('catalogue')

    context = {
        'form': form,
        'car': car,
        'car_id': car_id,
    }

    return render(request, 'car-delete.html', context)


def profile_details(request):
    profile = get_profile()
    cars = Car.objects.all()
    total_price = 0

    for car in cars:
        total_price += car.price

    context = {
        'profile': profile,
        'total_price': total_price,
    }

    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def profile_delete(request):
    profile = get_profile()
    cars = Car.objects.all()

    if request.method == 'POST':
        profile.delete()
        cars.delete()
        return redirect('home page')

    return render(request, 'profile-delete.html')
