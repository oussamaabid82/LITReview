from django.conf import settings
from django.db import models


class BookArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=8192, blank=True)

class Criticize(models.Model):
    title = models.CharField(max_length=200)
    description =models.CharField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    
class PhotoBook(models.Model):
    image = models.ImageField()
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


