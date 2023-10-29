from django.db import models
from django.contrib.auth.models import User



class BookCover(models.Model):
    cover = models.CharField(max_length=255)
    
    def __str__(self):
        return self.cover


class Book(models.Model):
    title = models.CharField(max_length=255)
    cover_img = models.ImageField(blank=True, default='')
    price = models.FloatField()
    rating = models.FloatField()
    type_cover = models.ForeignKey(BookCover, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    def __str__(self):
        return self.title
    
    
