from django import forms
from django.forms import NumberInput
from . import models
from .models import *


class AddAd(forms.ModelForm):
    # category = forms.ChoiceField(choices=[(item.pk, item) for item in Category.objects.all()])
    # subcategory = forms.ChoiceField(choices=[(item.pk, item) for item in Subcategory.objects.filter(category)])

    class Meta():
        model = Annonce
        fields = '__all__'
        exclude = ['user',]

    def __init__(self, *args, **kwargs):
        super(AddAd, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': "form-control"})

