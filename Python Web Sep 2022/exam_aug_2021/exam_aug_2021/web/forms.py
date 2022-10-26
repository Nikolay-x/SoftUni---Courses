from django import forms

from exam_aug_2021.web.models import Profile, Book


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),

            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),

            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }
            ),

            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            ),
        }


class EditBookForm(AddBookForm):
    pass


class ProfileEditForm(ProfileCreateForm):
    pass


class ProfileDeleteForm(ProfileCreateForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
