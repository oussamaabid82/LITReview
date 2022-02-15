from django import forms
from django.contrib.auth import get_user_model


CHOICES = [('0','0'), ('1','1'), ('2','2'),
           ('3','3'), ('4','4'), ('5','5'),
         ]
User = get_user_model()

class TicketForm(forms.Form):
    title = forms.CharField(max_length=200, label='title')
    description = forms.CharField(max_length=800, widget=forms.Textarea, label='description')
    image = forms.ImageField()

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=200, label='title')
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='rating')
    commentaire = forms.CharField(max_length=800, widget=forms.Textarea, label='commentaire')

class DeleteReviewForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['following']