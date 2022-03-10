from django.conf import settings
from django.db import models


class Ticket(models.Model):
    title_ticket = models.CharField(max_length=128)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="media", null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    RATING_RANGE = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE, null=True)
    title_review = models.CharField(max_length=128, null=True)
    content = models.TextField(max_length=5000)
    rating = models.CharField(max_length=11, choices=RATING_RANGE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)
