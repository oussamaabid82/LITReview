from django import forms
from . import models

CHOICES = [('-0','-0'), ('-1','-1'), ('-2','-2'),
           ('-3','-3'), ('-4','-4'), ('-5','-5'),
         ]

class BookArticleForm(forms.ModelForm):
    class Meta:
        model = models.BookArticle
        fields = ['title', 'description']

class CriticizeForm(forms.Form):
        title = forms.CharField(max_length=63, label='Titre')
        rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
        commentaire = forms.CharField(max_length=63, label='commentaire')

class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.PhotoBook
        fields = ['image']