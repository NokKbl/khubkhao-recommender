from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from khubkhaoapp.models import Category,EthnicFood, Food
from django.db.models import Q


class HomeView(TemplateView):
    template_name = 'registration/login.html'


class IndexView(TemplateView):
    template_name = 'khubkhaoapp/index.html'
    def get_context_data(self,*args,**kwargs):
        context = super(IndexView,self).get_context_data(*args, **kwargs)
        food_list = Food.objects.all()
        category_list = Category.objects.all()
        ethnic_list = EthnicFood.objects.all()
        context = {
            'food_list': food_list,
            'category_list': category_list,
            'ethnic_list': ethnic_list,
        }
        return context


def IndexResultView(request):
    if request.method == "POST" :
        my_ethnic = request.POST.getlist('ethnic_name')
        my_category = request.POST.getlist('category_name')
    selected_ethnic = EthnicFood.objects.filter(id__in=my_ethnic)
    selected_category = Category.objects.filter(id__in=my_category)
    if not selected_category.exists() and not selected_ethnic.exists():
        food_list = Food.objects.all()
    elif not selected_category.exists() or not selected_ethnic.exists():
        food_list = Food.objects.filter(Q(ethnic_food_name__in=selected_ethnic)|Q(category__in=selected_category)).distinct()
    else :
        food_list = Food.objects.filter(ethnic_food_name__in=selected_ethnic).filter(category__in=selected_category).distinct()
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    return render(request, 'khubkhaoapp/index.html', context)
