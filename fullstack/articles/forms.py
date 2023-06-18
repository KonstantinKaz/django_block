from django import forms
from channels.models import Channel
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['channel', 'article_title', 'article_description']
        widgets = {
            'channel': forms.Select(attrs={'class': 'form-control'}),
            'article_title': forms.TextInput(attrs={'class': 'form-control'}),
            'article_description': forms.Textarea(attrs={'class': 'form-control'}),
        }
