from django import forms
from authentication.models import UserFollows

CHOICES = [('0','0'), ('1','1'), ('2','2'),
           ('3','3'), ('4','4'), ('5','5'),
         ]

class TicketForm(forms.Form):
    title = forms.CharField(max_length=200, label='Titre')
    description = forms.CharField(max_length=800, widget=forms.Textarea, label='Déscription')
    image = forms.ImageField(required=False)

class ReviewForm(forms.Form):
    title = forms.CharField(max_length=200, label='title')
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label='rating')
    commentaire = forms.CharField(max_length=800, widget=forms.Textarea, label='commentaire')

class DeleteReviewForm(forms.Form):
    delete_blog = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['follows']
