from django import forms

from app import models


class PersonForm(forms.ModelForm):
    class Meta:
        model = models.Chat
        fields = ["requirements"]
        widgets = {
            "requirements": forms.Textarea(attrs={"cols": 100, "rows": 20}),
        }
