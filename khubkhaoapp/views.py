from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Q
from enum import Enum
from khubkhaoapp.models import Category, EthnicFood, Food
import logging

logger = logging.getLogger(__name__)


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


def logging_user(request,selected_ethnic,selected_category):
    '''
    Logging activity that user select type of ethnic food, category.
    '''
    user_ip = get_client_ip(request)
    category = str(selected_category)
    ethnic = str(selected_ethnic)

    if check_authenticated(request):
        user_id = request.user.id
        username = request.user.get_full_name()

        if not selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s id: %d user: %s didn\'t selected' % (user_ip,user_id,username))
        elif selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s id: %d user: %s is selected Category%s' % (user_ip,user_id,username,category))
        elif not selected_category.exists() and selected_ethnic.exists():
            logger.info('ip: %s id: %d user: %s is selected EthnicFood%s' % (user_ip,user_id,username,ethnic))
        else:
            logger.info('ip: %s id: %d user: %s is selected EthnicFood%s and Category%s ' % (user_ip,user_id,username,ethnic,category))
    else:
        if not selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s Guest didn\'t selected' % (user_ip))
        elif selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s Guest is selected Category%s' % (user_ip,category))
        elif not selected_category.exists() and selected_ethnic.exists():
            logger.info('ip: %s Guest is selected EthnicFood%s' % (user_ip,ethnic))
        else:
            logger.info('ip: %s Guest is selected EthnicFood%s and Category%s ' % (user_ip,ethnic,category))

        
def sort_food(unsorted_food):
    '''
    Sort food by overall rate.
    '''
    return sorted(unsorted_food, key = lambda food: food.set_total_rate(), reverse=True)[:25]


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


def check_authenticated(request):
    if request.user.is_authenticated and not request.user.is_anonymous:
        return True
    return False


class HomeView(TemplateView):
    template_name = 'registration/login.html'


def IndexView(request):
    '''
    Initial template when user get into KHUBKHAO-RECOMMENDER.
    '''
    user_ip = get_client_ip(request)
    template_name = 'khubkhaoapp/index.html'
    if check_authenticated(request):
        user_id = request.user.id
        username = request.user.get_full_name()
        logger.info('ip: %s id: %d user: %s have been using webpage ' % (user_ip,user_id,username))
        if request.method == "POST":
            my_vote = request.POST.get('rate_star')
            pk_and_vote = my_vote.split(',')
            vote_food(request,pk_and_vote[0],pk_and_vote[1])
            logger.info('ip: %s id: %d user: %s have been vote food for %s ' % (user_ip,user_id,username,pk_and_vote[1]))
    else:
        logger.info('ip: %s Guest have been using webpage' % user_ip)
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
        logging_user(request,selected_ethnic,selected_category)
        food_list = filter_food(selected_ethnic,selected_category)
    else:
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
    return render(request,template_name, context)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
