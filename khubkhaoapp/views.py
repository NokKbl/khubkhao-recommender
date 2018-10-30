from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
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

class IndexView(TemplateView):
    template_name = 'khubkhaoapp/index.html'
    
    def get_context_data(self,*args,**kwargs):
        context = super(IndexView,self).get_context_data(*args, **kwargs)
        # num = None
        # some_list = [
        #     random.randint(0,100), 
        #     random.randint(0,1000),
        #     random.randint(0,1000)
        # ]
        # condition_bool_item = False
        # if condition_bool_item:
        #     num = random.randint(0,1000)
        context ={
            # 'num': num,
            # 'some_list': some_list,
            # 'html_var': 'this is variable',
        }
        return context