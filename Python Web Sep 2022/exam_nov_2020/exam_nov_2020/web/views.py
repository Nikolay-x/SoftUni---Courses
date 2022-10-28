from django.shortcuts import render, redirect

from exam_nov_2020.web.forms import CreateRecipeForm, EditRecipeForm, DeleteRecipeForm
from exam_nov_2020.web.models import Recipe


# Create your views here.


def home_page(request):
    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == 'GET':
        form = CreateRecipeForm()
    else:
        form = CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, 'create.html', context)


def edit_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).get()

    if request.method == 'GET':
        form = EditRecipeForm(instance=recipe)
    else:
        form = EditRecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'recipe_id': recipe_id,
    }

    return render(request, 'edit.html', context)


def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).get()

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)

    else:
        form = DeleteRecipeForm(request.POST, instance=recipe)
        recipe.delete()
        return redirect('home page')

    context = {
        'form': form,
        'recipe_id': recipe_id,
    }

    return render(request, 'delete.html', context)


def details_recipe(request, recipe_id):
    recipe = Recipe.objects.filter(pk=recipe_id).get()
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'recipe_id': recipe_id,
        'ingredients': ingredients,
    }

    return render(request, 'details.html', context)
