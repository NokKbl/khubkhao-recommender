from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from khubkhaoapp.models import Category,EthnicFood, Food

class IndexTemplateView(TemplateView):
    template_name = 'khubkhaoapp/index.html'
    def get_context_data(self,*args,**kwargs):
        context = super(IndexTemplateView,self).get_context_data(*args, **kwargs)
        food_list = Food.objects.all()
        category_list = Category.objects.all()
        ethnic_list = EthnicFood.objects.all()
        context = {
            'food_list': food_list,
            'category_list': category_list,
            'ethnic_list': ethnic_list,
        }
        return context