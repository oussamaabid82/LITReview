from django.conf import settings
from django.db import models


class Photo(models.Model):
    image = models.ImageField()
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Ticket(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
