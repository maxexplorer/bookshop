from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField(null=True)
    author = models.CharField(max_length=100, null=True)

    def get_url(self):
        return reverse('book_detail', args=[self.id])

    def __str__(self):
        return f'Title: {self.title}, rating: {self.rating}, author: {self.author}'




