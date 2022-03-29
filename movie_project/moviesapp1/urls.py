from django.urls import path
from . import views

app_name = 'movies_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('movies/<int:x_id>/', views.details1, name='details1'),
    path('add/', views.add_movie, name='add_movie'),
    path('updates/<int:id>/', views.updates, name='updates'),
    path('delete/<int:id>/', views.delete, name='delete')
]
