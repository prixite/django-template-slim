from django import forms

from app import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ["name", "tagline"]
