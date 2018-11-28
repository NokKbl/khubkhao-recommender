from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from khubkhaoapp.models import Category, EthnicFood, Food
from django.db.models import Q
from enum import Enum

class HomeView(TemplateView):
    template_name = 'registration/login.html'

class Rate(Enum):
    ONE = 20
    TWO = 40
    THREE = 60
    FOUR = 80
    FIVE = 100

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
    '''
    Get ethnic from user then filter EhtnicFood.
    '''
    return EthnicFood.objects.filter(id__in=ethnic)

def filter_category(category):
    '''
    Get category from user then filter Category.
    '''
    return Category.objects.filter(id__in=category)

def filter_food(selected_ethnic,selected_category):
    '''
    Get selected_ethnic and selected_category from user then filter Food.
    '''
    if not selected_category.exists() and not selected_ethnic.exists():
        return Food.objects.all()
    elif not selected_category.exists() or not selected_ethnic.exists():
        return Food.objects.filter(Q(ethnic_food_name__in=selected_ethnic) | Q(
            category__in=selected_category)).distinct()
    return Food.objects.filter(ethnic_food_name__in=selected_ethnic).filter(
        category__in=selected_category).distinct()

def sort_food(unsort_food):
    '''
    Sort food by overall rate.
    '''
    return sorted(unsort_food, key = lambda food: food.compute_total_rate(), reverse=True)[:25]

def check_vote(request,food_set):
    '''
    If user vote food then set check to false.
    '''
    for food in food_set:
        array = food.get_user_pk().split(',')
        if(str(request.user.pk) in array):
            food.set_check_false()
        else:
            food.set_check_true()
        food.save()


def vote_food(request,pk_food,vote):
    '''
    If user vote food then count of vote in each food is increase.
    '''
    vote_scores = vote_value(vote).value
    food = Food.objects.get(pk=pk_food)
    food.add_user_count()
    food.set_user_rate(vote_scores)
    food.add_user_pk(request.user.pk)
    food.save()

def IndexView(request):
    '''
    Initial template when user get into KHUBKHAO-RECOMMENDER.
    '''
    template_name = 'khubkhaoapp/index.html'
    if request.method == "POST" and request.user.is_authenticated and not request.user.is_anonymous:
        my_vote = request.POST.get('rate_star')
        pk_and_vote = my_vote.split(',')
        vote_food(request,pk_and_vote[0],pk_and_vote[1])
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
    return render(request, template_name, context)
    
def IndexResultView(request):
    '''
    If user filter food then POST request to change result of food.
    '''
    template_name = 'khubkhaoapp/index.html'
    if request.method == "POST":
        my_ethnic = request.POST.getlist('ethnic_name')
        my_category = request.POST.getlist('category_name')
        selected_ethnic = filter_ethnic(my_ethnic)
        selected_category = filter_category(my_category)
        food_list = filter_food(selected_ethnic,selected_category)
        check_vote(request,food_list)
        food_list = sort_food(food_list)

    else:
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
    return render(request,template_name, context)