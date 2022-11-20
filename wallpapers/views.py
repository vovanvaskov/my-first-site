from django.shortcuts import render
from .models import Wall, Category, Device
from django.views.generic import ListView, DetailView

device_navigation = Device.objects.all()
category_navigation = Category.objects.all()

class WallpapersHome(ListView):
    paginate_by = 12
    model = Wall
    template_name = 'wallpapers/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home page'
        context['nav'] = device_navigation
        return context

class DevicesWalls(ListView):
    paginate_by = 12
    model = Wall
    template_name = 'wallpapers/device.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['object_list'][0].device)
        context['category_nav'] = category_navigation
        context['device'] = int(context['object_list'][0].device.id)
        return context

    def get_queryset(self):
        return Wall.objects.filter(device__id = self.kwargs['device_id'])

class CategoriesWalls(ListView):
    paginate_by = 12
    model = Wall
    template_name = 'wallpapers/device.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['object_list'][0].device)
        context['category_nav'] = category_navigation
        context['device'] = int(context['object_list'][0].device.id)
        return context

    def get_queryset(self):
        return Wall.objects.filter(device__id = self.kwargs['device_id'], category__id = self.kwargs['category_id'])

class ShowWall(DetailView):
    model = Wall
    template_name = 'wallpapers/a_wall.html'
    context_object_name = 'wall'
    pk_url_kwarg = 'wall_id'
