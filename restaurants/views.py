from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Restaurant
from django.db.models import Q



class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = Restaurant.objects.filter(
                Q(category__iexact=slug) |
                Q(category__icontains=slug) 
            ) 
        else:
            queryset = Restaurant.objects.all()           
        return queryset 



class RestaurantDetailView(DetailView):
    queryset = Restaurant.objects.all()            

    # def get_context_data(self, *args, **kwargs):
    #     print(self.kwargs)
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(Restaurant, id=rest_id)
    #     return obj