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
    image = forms.ImageField()

    class Meta:
        model = Ticket
        fields = ['title_ticket', 'description', 'image']


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=RATING_RANGE, widget=forms.RadioSelect())

    class Meta:
        model = Review
        fields = ['title_review', 'rating', 'content']


class FollowUsersForm(forms.ModelForm):

    class Meta:
        model = UserFollows
        fields = ['follows']


class SearchUserForm(forms.Form):
    username = forms.CharField(max_length=100)
