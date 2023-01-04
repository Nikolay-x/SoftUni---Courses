from django import forms

from equip_mgmt.spares.models import Spares


class SparesAddForm(forms.ModelForm):
    class Meta:
        model = Spares
        exclude = ('pump', )
