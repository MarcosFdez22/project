from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Author(models.Model):
    first_name= models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=50)
    raiting = models.IntegerField(
        validators= [MinValueValidator(0),MaxValueValidator(10)]
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bestSelling = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} ({self.raiting})"