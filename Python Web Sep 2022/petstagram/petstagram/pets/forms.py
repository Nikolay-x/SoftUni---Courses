from django import forms

from petstagram.core.forms_mixins import DisabledFormMixin
from petstagram.pets.models import Pet


# 'ModelForm' and 'Form':
# - 'ModelForm' binds to models
# - 'Form' is detached from models
class PetBaseForm(forms.ModelForm):
    # Another variant to override the widgets:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['name'].widget.attrs['placeholder'] = 'Pet name'

    class Meta:
        model = Pet
        # fields = '__all__'  # (not the case, we want to skip 'slug')
        fields = ('name', 'date_of_birth', 'personal_photo')
        # exclude = ('slug',)
        labels = {
            'name': 'Pet Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet name',
                }
            ),

            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),

            'personal_photo': forms.URLInput(
                attrs={
                    'placeholder': 'Link to image',
                }
            ),
        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(PetBaseForm):  # PetEditForm needs to inherit DisabledFormMixin the below code to work
    # disabled_fields = ('name',)
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # print(self.__dict__)
    #     self._disable__fields()
    pass


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'personal_photo', 'date_of_birth')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(self.__dict__)
        self._disable__fields()

    def save(self, commit=True):
        # super().save()  # easy way to reach 'commit' in Django code
        if commit:
            self.instance.delete()
        else:
            pass

        return self.instance
