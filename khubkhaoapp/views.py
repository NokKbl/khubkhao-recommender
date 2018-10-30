from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from khubkhaoapp.models import Category, Food

# Create your views here.
class FoodListView(ListView):
    template_name = 'bookshelf/bookshelf_list.html'
    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if(slug):
            # queryset = Library.objects.filter(
            #     Q(category__iexact=slug) |
            #     Q(category__icontains=slug)
            # )
            queryset = Food.get_veggie_type.all()
        else:
            queryset = Food.objects.all()
        return queryset

class AllFoodListView(ListView):
    queryset = Food.objects.all()
    template_name = 'khubkhaoapp/food_list.html'

def IndexView(request):
    context = {

    }
    return render(request, 'khubkhaoapp/index.html', context)