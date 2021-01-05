from django import forms
from django.db import models

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['main_text', 'create_img']

        widgets = {
            'main_text': forms.TextInput(attrs={'class': 'form-control', 'rows':'7', 'cols':'40', 'maxlength':'150'}),
            'create_img' : forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

        labels = {
            'main_text': '본문 내용',
            'create_img': '사진',
        }