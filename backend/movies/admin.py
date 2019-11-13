from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'plot', 'release_date', 'running_time', 'views', 'likes', 'rating')

admin.site.register(Movie, MovieAdmin)
