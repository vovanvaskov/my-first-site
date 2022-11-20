from django.urls import path

from . import views

urlpatterns = [
    path('', views.WallpapersHome.as_view(), name = 'index'),
    path('device/<int:device_id>/', views.DevicesWalls.as_view(), name = 'device'),
    path('device/<int:device_id>/category/<int:category_id>/', views.CategoriesWalls.as_view(), name = 'category'),
    path('wall/<int:wall_id>/', views.ShowWall.as_view(), name = 'wall'),
]
