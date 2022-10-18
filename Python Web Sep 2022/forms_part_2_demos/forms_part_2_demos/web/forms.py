import uuid

from django import forms
from django.core.exceptions import ValidationError

from forms_part_2_demos.web.model_validators import validate_max_todos_per_person
from forms_part_2_demos.web.models import Todo, Person
from forms_part_2_demos.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(
          validate_text,
        ),
        error_messages={
            'required': 'Todo text must be set!'
        }
    )

    is_done = forms.BooleanField(
        required=False,
    )

    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
            # validate_priority,
            # MinValueValidator(1),
            # MaxValueValidator(10),
        ),
    )

    # def clean_text(self):
    #     pass
    #
    # def clean_is_done(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #     # raise ValidationError('Error!!!')


# Model forms are inheriting the model validators,
# but they are also able to add their own validators
class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    # 'clean' methods can be used for data transformations and validations
    def clean_text(self):
        '''
        Used for:
        1. Transform data in desired format
        2. Validation
        '''
        return self.cleaned_data['text'].lower()

    # 1. Transform data into desired format/form/state
    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        try:
            validate_max_todos_per_person(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')  # like this the validation is skipped

            # The below is not solution
            # self.cleaned_data['assignee'] = Person.objects.get(name='Unassigned')
            # assignee = self.clean_assignee()
        return assignee

    # 2. Validation
    # def clean_assignee(self):
    #     # print(self.cleaned_data['assignee'])
    #     assignee = self.cleaned_data['assignee']
    #     # if assignee.todo_set.count() >= Todo.MAX_TODOS_COUNT_PER_PERSON:
    #     #     raise ValidationError(f'{assignee} already has max todos assigned')
    #     validate_max_todos_per_person(assignee)
    #     return assignee

    # Just for demo
    # def clean(self):
    #     pass


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    # def clean_profile_image(self):
    #     profile_image = self.cleaned_data['profile_image']
    #     # profile_image.name = self.cleaned_data['name']
    #     profile_image.name = str(uuid.uuid4())
    #     return profile_image

    # def clean(self):
    #     super().clean()  # After this, all values are in 'cleaned_data'
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']
