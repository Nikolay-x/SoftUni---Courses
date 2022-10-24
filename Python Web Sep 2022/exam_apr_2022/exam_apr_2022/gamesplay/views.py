from django.shortcuts import render, redirect

from exam_apr_2022.gamesplay.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, \
    EditProfileForm
from exam_apr_2022.gamesplay.models import Profile, Game


# Create your views here.


def homepage(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile

    }

    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def dashboard(request):
    games = Game.objects.all()

    context = {
        'games': games,
    }

    return render(request, 'dashboard.html', context)


def create_game(request):
    if request.method == 'GET':
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
    }

    return render(request, 'create-game.html', context)


def details_game(request, id):
    game = Game.objects\
        .filter(id=id)\
        .get()

    context = {
        'game': game,
        'id': id,
    }

    return render(request, 'details-game.html', context)


def edit_game(request, id):
    game = Game.objects\
        .filter(id=id)\
        .get()

    if request.method == 'GET':
        form = EditGameForm(instance=game)
    else:
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'edit-game.html', context)


# def delete_game(request, id):
#     game = Game.objects.get(id=id)
#
#     if request.method == 'POST':
#         game.delete()
#         return redirect('dashboard')
#
#     form = DeleteGameForm(instance=game)
#
#     context = {
#         'form': form,
#         'game': game,
#     }
#
#     return render(request, 'delete-game.html', context)


def delete_game(request, id):
    game = Game.objects.get(id=id)

    if request.method == 'GET':
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        game.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'game': game,
    }

    return render(request, 'delete-game.html', context)


def details_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()
    games_count = Game.objects.all().count()
    rating = 0.0

    if games_count == 0:
        avg_rating = '0.0'
    else:
        for game in games:
            rating += game.rating

        avg_rating = f'{rating / games_count:.1f}'

    context = {
        'profile': profile,
        'avg_rating': avg_rating,
        'games_count': games_count,
    }

    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        form = EditProfileForm(instance=profile)
    else:
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
    }

    return render(
        request,
        'edit-profile.html',
        context
    )


def delete_profile(request):
    profile = Profile.objects.first()
    games = Game.objects.all()

    if request.method == 'POST':
        profile.delete()
        games.delete()
        return redirect('home page')

    return render(request, 'delete-profile.html')
