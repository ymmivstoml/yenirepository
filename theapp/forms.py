from django import forms
from .models import Dumdatas

class DataForm(forms.ModelForm):

    class Meta:

        model = Dumdatas
        fields = ('kartid',)
