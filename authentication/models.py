# from django.conf import settings
# from django.contrib.auth.models import User, Group
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class UserFollows(AbstractUser):
    USER = 'USER'
    FORLLOWED_USER = 'FORLLOWED_USER'


    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit'
    )

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.USER:
    #         group = Group.objects.get(name='users')
    #         group.user_set.add(self)
    #     elif self.FORLLOWED_USER:
    #         group = Group.objects.get(name='followed_users')
    #         group.user_set.add(self)


# class UserFollows(User):
#     user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='following')
#     followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='followed_by')
#     follows = models.ManyToManyField('self', symmetrical=False, verbose_name='suit')
#     class Meta:
#         unique_together = ('user','followed_user',)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.user:
#             group = Group.objects.get(name='users')
#             group.user_set.add(self)
#         elif self.followed_user:
#             group = Group.objects.get(name='followed_users')
#             group.user_set.add(self)
