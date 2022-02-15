from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserFollows(User):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='followed_by')
    follows = models.ManyToManyField('self', symmetrical=True, verbose_name='suit')
    class Meta:
        unique_together = ('user','followed_user',)
        
    # # CREATOR = 'CREATOR'
    # # SUBSCRIBER = 'SUBSCRIBER'

    # CHOICES = (
    #     ('CREATOR', 'Créateur'),
    #     # (SUBSCRIBER, 'Abonné'),
    # )
    
    # role = models.CharField(max_length=30, choices=CHOICES, verbose_name='rôle')
    # follows = models.ManyToManyField(
    #     'self', 
    #     # limit_choices_to={'role': 'CREATOR'},
    #     symmetrical=False,
    #     verbose_name='suit'
    # )

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
        # if self.role == self.CREATOR:
        #     group = Group.objects.get(name='creators')
        #     group.user_set.add(self)
        # elif self.role == self.SUBSCRIBER:
        #     group = Group.objects.get(name='subscribers')
        #     group.user_set.add(self)
