from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "category", "image", "description"]
        widgets = {
            'category': forms.Select(choices=Item.CATEGORY_CHOICES),
            'users': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'image': 'Item Image',
        }
        help_texts = {
            'image': 'Upload an image for the item (optional)',
        }
        error_messages = {
            'image': {
                'invalid': ("Image files only please."),
            },
        }
