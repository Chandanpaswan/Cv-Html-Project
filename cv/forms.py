from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "autocomplete": "name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@company.com", "autocomplete": "email"}),
            "phone": forms.TextInput(attrs={"placeholder": "Optional", "autocomplete": "tel"}),
            "message": forms.Textarea(attrs={"placeholder": "What would you like to work on?", "rows": 5}),
        }


class CVUploadForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = []
