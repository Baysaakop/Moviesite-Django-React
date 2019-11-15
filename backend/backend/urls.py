from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies import views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet, 'movies')
router.register(r'home', views.HomeViewSet, 'home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
