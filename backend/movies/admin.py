from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'plot', 'release_date', 'running_time', 'views', 'likes', 'rating', 'created_at', 'created_by', 'updated_at', 'updated_by')

admin.site.register(Movie, MovieAdmin)
