from django import forms

from exam_apr_2022.gamesplay.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('email', 'age', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'category', 'rating', 'max_level', 'image_url', 'summary')
        labels = {
            'title': 'Title',
            'category': 'Category',
            'rating': 'Rating',
            'max_level': 'Max Level',
            'image_url': 'Image URL',
            'summary': 'Summary',
        }


class EditGameForm(CreateGameForm):
    pass


class DeleteGameForm(CreateGameForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
