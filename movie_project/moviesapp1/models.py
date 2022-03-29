from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    ima = models.ImageField(upload_to='gallery', blank=True, null=True)

    def __str__(self):
        return self.name

# Create your models here.
