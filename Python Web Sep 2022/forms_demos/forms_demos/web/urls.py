from django.urls import path

from forms_demos.web.views import index_form, index_model_form, related_models_demo

urlpatterns = (
    path('', index_form, name='index_form'),
    path('modelforms/', index_model_form, name='model forms'),
    path('demo/relations', related_models_demo, name=' demo relations')
)
