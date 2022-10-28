from django.urls import path

from exam_nov_2020.web.views import home_page, create_recipe, edit_recipe, \
    delete_recipe, details_recipe

urlpatterns = (
    path('', home_page, name='home page'),
    path('create/', create_recipe, name='create recipe'),
    path('edit/<int:recipe_id>/', edit_recipe, name='edit recipe'),
    path('delete/<int:recipe_id>/', delete_recipe, name='delete recipe'),
    path('details/<int:recipe_id>/', details_recipe, name='details recipe'),
)
