from django import forms

from exam_nov_2020.web.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),

            'ingredients': forms.TextInput(
                attrs={
                    'placeholder': 'Ingredient1, Ingredient2, Ingredient3...',
                }
            ),

            'time': forms.NumberInput(
                attrs={
                    'placeholder': 'cooking time in min'
                }
            ),
        }


class EditRecipeForm(CreateRecipeForm):
    pass


class DeleteRecipeForm(CreateRecipeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
