from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    raiting = models.IntegerField(
        validators= [MinValueValidator(0),MaxValueValidator(10)]
    )
    author = models.CharField(null=True, max_length=100)
    bestSelling = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} ({self.raiting})"