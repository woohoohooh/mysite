from django import forms
from .models import Post
from django.forms import MultipleChoiceField, ChoiceField, Form

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('product', 'currency', 'balance_users', 'balance_reserve_fund', 'description', 'archive')


