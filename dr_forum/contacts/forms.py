from django import forms
from django.core.exceptions import ValidationError

from contacts.models import Contacts


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'required': 'required'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'required': 'required'
            }),
        }

        error_messages = {
            'name': {
                'required': '⚠️ Please enter your name.',
            },
            'email': {
                'required': '⚠️ Email required.',
            },
            'subject': {
                'required': '⚠️ Enter subject.',
            },
            'message': {
                'required': '⚠️ Enter message.',
            },
        }
