from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = [
            'author',
            'postCategory',
            'title',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        title = cleaned_data.get("title")
        if title == text:
            raise ValidationError(
                "Текст новости не должен повторять заголовок."
            )
        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError(
                "Заголовок должен начинаться с заглавной буквы"
            )
        return title
