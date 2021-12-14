from django.db import models
from django.contrib.auth import get_user_model


class Book (models.Model):
    title = models.CharField(max_length=64, default= 'None')
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=25)
    summary = models.TextField()
    available = models.BooleanField(default = True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title