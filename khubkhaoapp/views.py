from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from khubkhaoapp.models import Category, EthnicFood, Food
from django.db.models import Q

# def get_total_rate(self):
#         float_price = float(self.original_rate)*0.8
#         float_user = float(self.user_rate)*0.2
#         float_price = float("{0:.2f}".format(float_price))
#         float_user = float("{0:.2f}".format(float_user))
#         return float_price+float_user

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
        food_list = sorted(unsorted_results, key = lambda food: food.get_total_rate(), reverse=True)[:25]
        
        # ======================== MAI THAVORN
        # for food in food_list:
        #     food.set_user_rate(100)
        # =======================Save THAVORN
        # food.save()

        # food_list = Food.objects.all().order_by('original_rate').reverse()[:10:2] #Menu 1 3 5 7 9
        # food_list = Food.objects.filter(original_rate__gt=F('user_rate')+78)
        # Company.objects.filter(num_employees__gt=F('num_chairs') * 2)
        category_list = Category.objects.all()
        ethnic_list = EthnicFood.objects.all()
        context = {
            'food_list': food_list,
            'category_list': category_list,
            'ethnic_list': ethnic_list,
        }
        return context


def IndexResultView(request):
    if request.method == "POST":
        my_ethnic = request.POST.getlist('ethnic_name')
        my_category = request.POST.getlist('category_name')
    selected_ethnic = EthnicFood.objects.filter(id__in=my_ethnic)
    selected_category = Category.objects.filter(id__in=my_category)
    if not selected_category.exists() and not selected_ethnic.exists():
        food_list = Food.objects.all()
    elif not selected_category.exists() or not selected_ethnic.exists():
        food_list = Food.objects.filter(Q(ethnic_food_name__in=selected_ethnic) | Q(
            category__in=selected_category)).distinct()
    else:
        food_list = Food.objects.filter(ethnic_food_name__in=selected_ethnic).filter(
            category__in=selected_category).distinct()
    unsorted_results = food_list
    food_list = sorted(unsorted_results, key = lambda food: food.get_total_rate(), reverse=True)[:25]
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    return render(request, 'khubkhaoapp/index.html', context)
