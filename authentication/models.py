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
    