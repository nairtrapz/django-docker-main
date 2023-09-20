from django import forms
from .models import MyModel

class MyForms (forms.ModelForm):
    class Meta:
        model = MyModel
        fields = "__all__"