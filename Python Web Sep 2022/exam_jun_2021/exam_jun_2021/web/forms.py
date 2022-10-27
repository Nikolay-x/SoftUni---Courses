from django import forms

from exam_jun_2021.web.models import Profile, Note


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

            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Content',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class EditNoteForm(AddNoteForm):
    pass


class NoteDeleteForm(AddNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
