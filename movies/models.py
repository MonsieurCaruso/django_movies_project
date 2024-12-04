from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    GENRE_CHOICES = [
        ('ACTION', 'Action'),
        ('COMEDY', 'Comedy'),
        ('DRAMA', 'Drama'),
        ('FANTASY', 'Fantasy'),
        ('HORROR', 'Horror'),
        ('MYSTERY', 'Mystery'),
        ('ROMANCE', 'Romance'),
        ('SCIFI', 'Science Fiction'),
        ('THRILLER', 'Thriller'),
        ('ANIMATION', 'Animation'),
        ('DOCUMENTARY', 'Documentary'),
        ('OTHER', 'Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField()
    genre = models.CharField(
        max_length=20,
        choices=GENRE_CHOICES,
        default='OTHER'
    )
    imdb_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titlefo