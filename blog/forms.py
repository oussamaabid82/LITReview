from attr import fields
from django import forms
from authentication.models import UserFollows
from .models import Review, Ticket

RATING_RANGE = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )


class TicketForm(forms.ModelForm):
    description = forms.CharField(max_length=800, widget=forms.Textarea, label='Déscription')
    image = forms.ImageField(required=False)
    class Meta:
        model = Ticket
        fields = ['description', 'image']
    
    # title = forms.CharField(max_length=200, label='Titre')
    # description = forms.CharField(max_length=800, widget=forms.Textarea, label='Déscription')
    # image = forms.ImageField(required=False)

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_RANGE, widget=forms.RadioSelect())
    class Meta:
        model = Review
        fields = ['rating', 'content']

class FollowUsersForm(forms.ModelForm):
    class Meta:
        model = UserFollows
        fields = ['follows']
