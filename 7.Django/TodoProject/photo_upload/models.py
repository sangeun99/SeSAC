from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.title}, {self.photo}"