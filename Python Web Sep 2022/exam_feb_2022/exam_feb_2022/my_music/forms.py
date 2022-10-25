from django import forms

from exam_feb_2022.my_music.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),

            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age',
                }
            ),
        }


class AddAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'album_name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),

            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),

            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }


class EditAlbumForm(AddAlbumForm):
    pass


class DeleteAlbumForm(AddAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
