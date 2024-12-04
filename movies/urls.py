from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('watchlist/', views.watchlist_view, name='watchlist'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]
