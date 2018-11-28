from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from khubkhaoapp.models import Category,EthnicFood, Food
from django.db.models import Q
from enum import Enum
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class HomeView(TemplateView):
    template_name = 'registration/login.html'

class Rate(Enum):
    ONE = 20
    TWO = 40
    THREE = 60
    FOUR = 80
    FIVE = 100

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def vote_value(raw_number):
    if(raw_number == "ONE") :
        return Rate.ONE
    elif(raw_number == "TWO") :
        return Rate.TWO
    elif(raw_number == "THREE") :
        return Rate.THREE
    elif(raw_number == "FOUR") :
        return Rate.FOUR
    else :
        return Rate.FIVE

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

def check_vote(request,food_set):
    for food in food_set:
        array = food.get_user_pk().split(',')
        if(str(request.user.pk) in array):
            food.set_check_false()
        else:
            food.set_check_true()
        food.save()


def vote_food(request,pk_food,vote):
    vote_scores = vote_value(vote).value
    food = Food.objects.get(pk=pk_food)
    food.add_user_count()
    food.set_user_rate(vote_scores)
    food.add_user_pk(request.user.pk)
    food.save()

def IndexView(request):
    template_name = 'khubkhaoapp/index.html'
    unsorted_results = Food.objects.all()
    check_vote(request,unsorted_results)
    food_list = sort_food(unsorted_results)
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    ip = get_client_ip(request)
    if request.user.is_authenticated and not request.user.is_anonymous:
        logger.info('ip: %s id: %d user: %s have been using webpage ' % (ip,request.user.id,request.user.get_full_name()))
    else:
        logger.info('ip: %s Guest have been using webpage' % ip)
    return render(request, template_name, context)
    
def IndexResultView(request):
    ip = get_client_ip(request)
    if request.method == "POST":
        my_ethnic = request.POST.getlist('ethnic_name')
        my_category = request.POST.getlist('category_name')
        if request.user.is_authenticated and not request.user.is_anonymous:
            logger.info('ip: %s id: %d user: %s is selected EhtnicFood%s and Category%s ' % (ip,request.user.id,request.user.get_full_name(),str(my_ethnic),str(my_category) ) )
        else:
            logger.info('ip: %s Guest is selected %s and %s ' % (ip,str(my_ethnic),str(my_category)))
    selected_ethnic = filter_ethnic(my_ethnic)
    selected_category = filter_category(my_category)
    food_list = filter_food(selected_ethnic,selected_category)
    check_vote(request,food_list)
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
    if request.method == "POST" and request.user.is_authenticated and not request.user.is_anonymous:
        my_vote = request.POST.get('rate_star')
        pk_and_vote = my_vote.split(',')
        vote_food(request,pk_and_vote[0],pk_and_vote[1])
    food_list = Food.objects.all()
    check_vote(request,food_list)
    food_list = sort_food(food_list)
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    ip = get_client_ip(request)
    logger.info('ip: %s id: %d user: %s have been vote food for %s ' % (ip,request.user.id,request.user.get_full_name(),pk_and_vote[1]))
    return render(request,'khubkhaoapp/index.html', context)


