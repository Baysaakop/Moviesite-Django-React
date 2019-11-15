from django.db import models
from django.contrib.auth.models import User
import datetime

class Movie(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    plot = models.TextField()
    release_date = models.DateField(null=True)
    running_time = models.IntegerField(default=90)    
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)    
    created_by = models.ForeignKey(User, null=True, related_name='movies', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, blank=True, null=True, related_name='+', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

