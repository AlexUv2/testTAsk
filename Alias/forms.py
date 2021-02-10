from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime


from .models import Alias, Target

class AliasForm(ModelForm):

    class Meta:
        model = Alias
        fields = "__all__"
        target = forms.ModelChoiceField(queryset=Target.objects.all())
        widgets = {
            'alias': forms.TextInput(attrs={'placeholder': 'New Alias'}),
            'start': forms.DateTimeInput(format=['%m/%d/%Y %H:%M:%S.%f'],
             attrs={'placeholder': 'Start time'}),
            'end': forms.DateTimeInput(format=['%m/%d/%Y %H:%M:%S.%f'],
             attrs={'placeholder': 'End time'}),
        }


    def clean(self):
        '''Cheking input date and raising errors if date is not correct '''
        cleaned_data = super(AliasForm, self).clean()
        start = cleaned_data.get('start')
        end = cleaned_data.get('end')
        target = cleaned_data.get('target')
        alias = cleaned_data.get('alias')

        aliases_obj = Alias.objects.all()

        for i in aliases_obj: #Ovarlaping save Alias
            if alias == i.alias:
                if target == i.target:
                    if (end > i.start and start < i.start) or (start < i.end and end > i.end):
                        raise forms.ValidationError (_('You can have only one Alias in this time'))

        if end <= start:
            raise forms.ValidationError (_('End time must be later than start time!'))
        elif end < timezone.now():
            raise forms.ValidationError (_('End time must be later than now!'))

        
class TargetForm(ModelForm):
    class Meta:
        model = Target
        fields = "__all__"
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'New Target'})
        }