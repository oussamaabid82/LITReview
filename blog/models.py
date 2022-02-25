from distutils.command.upload import upload
from django.conf import settings
from django.db import models
from PIL import Image


class Ticket(models.Model):
    title_ticket = models.CharField(max_length=128)
    description = models.TextField(max_length=5000)
    image = models.ImageField(upload_to="media", null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributor', related_name='ticket_contributions')
    date_created = models.DateTimeField(auto_now_add=True)
    
    # IMAGE_MAX_SIZE = (200, 200)

    # def resize_image(self):
    #     image = Image.open(self.image)
    #     image.thumbnail(self.IMAGE_MAX_SIZE)
    #     image.save(self.image.path)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     self.resize_image()
    
class Review(models.Model):
    RATING_RANGE = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    ticket = models.ForeignKey(to=Ticket,on_delete=models.CASCADE, null=True)
    title_review = models.CharField(max_length=128, null=True)
    content = models.TextField(max_length=5000)
    rating = models.CharField(max_length=11, choices=RATING_RANGE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributor', related_name='review_contributions')
    date_created = models.DateTimeField(auto_now_add=True)
  
    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)

class BlogContributor(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    contribution = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('contributor', 'review', 'ticket',)
