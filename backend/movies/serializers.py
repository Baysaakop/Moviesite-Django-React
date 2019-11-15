from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'plot', 'release_date', 'running_time', 'views', 'likes', 'rating', 'created_at', 'created_by', 'updated_at', 'updated_by')