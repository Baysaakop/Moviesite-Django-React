from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    plot = models.TextField()
    release_date = models.DateField(null=True)
    running_time = models.IntegerField(default=90)    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    rating = models.FloatField()

    def __str__(self):
        return self.title

