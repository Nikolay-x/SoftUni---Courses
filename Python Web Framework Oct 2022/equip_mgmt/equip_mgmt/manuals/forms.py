from django import forms

from equip_mgmt.core.utils import DateInput
from equip_mgmt.manuals.models import Manual


class ManualAddForm(forms.ModelForm):
    class Meta:
        model = Manual
        exclude = ('pump', )
        widgets = {
            'issue_date': DateInput(),
            'expiry_date': DateInput(),
        }


class ManualDeleteForm(ManualAddForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
