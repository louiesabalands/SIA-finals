from django.db import models

# Create your models here.
class Movie(models.Model):
    Movie_id = models.AutoField(primary_key=True)
    MovieTitle = models.CharField(max_length=100)
    Genre = models.DecimalField(max_digits=10, decimal_places=2)
    ReleaseYear = models.IntegerField()
    Director = models.CharField(max_length=100)
    Rating = models.DecimalField(max_digits=3, decimal_places=1)
    Description = models.TextField()
    Status = models.CharField(max_length=20, choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], default='Available')
    DateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.MovieTitle
    