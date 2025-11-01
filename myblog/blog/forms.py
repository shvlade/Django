from django import forms

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']
        widgets = {
            'author': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'comment-input'
            }),
            'text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Оставьте ваш комментарий...',
                'class': 'comment-textarea'
            }),
        }
        labels = {
            'author': 'Ваше имя',
            'text': 'Комментарий'
        }
class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=100,
        required=False,
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Поиск по заголовку и содержанию...',
            'class': 'search-input',
            'name': 'query'  # Добавляем явное имя поля
        })
    )