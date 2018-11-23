from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from khubkhaoapp.models import Category, EthnicFood, Food
from django.db.models import Q

class IndexView(TemplateView):
    template_name = 'khubkhaoapp/index.html'

    # def get_db_prep_value(self, value, connection, prepared=False):
    #     value = super().get_db_prep_value(value, connection, prepared)
    #     if value is not None:
    #         return connection.Database.Binary(value)
    #     return value

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        
        # food_list = Food.objects.all().order_by(
        #     'original_rate').reverse()[:25]  # Menu 1-25
        
        unsorted_results = Food.objects.all()
        food_list = sorted(unsorted_results, key = lambda food: food.compute_total_rate(), reverse=True)[:25]
        
        # ======================== MAI THAVORN
        # for food in food_list:
        #     food.set_user_rate(100)
        # =======================Save THAVORN
        # food.save()

        # food_list = Food.objects.all().order_by('original_rate').reverse()[:10:2] #Menu 1 3 5 7 9
        # food_list = Food.objects.filter(original_rate__gt=F('user_rate')+78)
        category_list = Category.objects.all()
        ethnic_list = EthnicFood.objects.all()
        context = {
            'food_list': food_list,
            'category_list': category_list,
            'ethnic_list': ethnic_list,
        }
        return context

def filter_ethnic(ethnic):
    return EthnicFood.objects.filter(id__in=ethnic)

def filter_category(category):
    return Category.objects.filter(id__in=category)

def filter_food(selected_ethnic,selected_category):
    if not selected_category.exists() and not selected_ethnic.exists():
        return Food.objects.all()
    elif not selected_category.exists() or not selected_ethnic.exists():
        return Food.objects.filter(Q(ethnic_food_name__in=selected_ethnic) | Q(
            category__in=selected_category)).distinct()
    return Food.objects.filter(ethnic_food_name__in=selected_ethnic).filter(
        category__in=selected_category).distinct()

def sort_food(unsort_food):
    return sorted(unsort_food, key = lambda food: food.compute_total_rate(), reverse=True)[:25]
            
def IndexResultView(request):
    if request.method == "POST":
        my_ethnic = request.POST.getlist('ethnic_name')
        my_category = request.POST.getlist('category_name')
    selected_ethnic = filter_ethnic(my_ethnic)
    selected_category = filter_category(my_category)
    food_list = filter_food(selected_ethnic,selected_category)
    food_list = sort_food(food_list)
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    return render(request, 'khubkhaoapp/index.html', context)

def IndexVoteView(request):
    if request.method == "POST":
        my_vote = request.POST.get('rate_star')
    pk_and_vote = my_vote.split(',')
    pk_and_vote[1] = float(pk_and_vote[1])*20
    food = Food.objects.get(pk=pk_and_vote[0])
    food.set_user_rate(pk_and_vote[1])
    food.add_user_count()
    food.save()

    food_list = Food.objects.all()
    food_list = sort_food(food_list)
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    return render(request,'khubkhaoapp/index.html', context)