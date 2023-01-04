from django import forms

from equip_mgmt.core.utils import DateInput
from equip_mgmt.m_activities.models import Activity


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ('pump', )
        widgets = {
            'due_date': DateInput(),
        }
