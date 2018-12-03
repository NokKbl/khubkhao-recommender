from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Q
from enum import Enum
import logging
from khubkhaoapp.models import Category, EthnicFood, Food


logger = logging.getLogger(__name__)


class Rate(Enum):
    """
    An enumeration for rates.
    """
    ONE = 20
    TWO = 40
    THREE = 60
    FOUR = 80
    FIVE = 100


def get_client_ip(request):
    """
    Get an IP of the user.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def vote_value(raw_number):
    """
    Get rate values from enumeration which can be [20, 40, 60, 80, 100].

    Args:
        raw_number (str): text which used to specify rate values.
    Returns:
        int: rate value which can be [20, 40, 60, 80, 100].
    """
    if(raw_number == "ONE") :
        return Rate.ONE.value
    elif(raw_number == "TWO") :
        return Rate.TWO.value
    elif(raw_number == "THREE") :
        return Rate.THREE.value
    elif(raw_number == "FOUR") :
        return Rate.FOUR.value
    else :
        return Rate.FIVE.value


def filter_ethnic(ethnic):
    """
    Filter ethnic foods which have been chosen from the user.

    Returns:
        EthinicFood: ethnic foods which have been chosen from the user.
    """
    return EthnicFood.objects.filter(id__in=ethnic)


def filter_category(category):
    """
    Filter categories which have been chosen from the user.

    Returns:
        Category: categories which have been chosen from the user.
    """
    return Category.objects.filter(id__in=category)


def filter_food(selected_ethnic,selected_category):
    """
    Filter food's criteria specified by the user.

    Args:
        selected_ethnic (EthinicFood): ethnic foods which have been chosen from user.
        selected_category (Category): categories which have been chosen from user.
    Returns:
        Food: food's criteria specified by the user.
    """
    if not selected_category.exists() and not selected_ethnic.exists():
        return Food.objects.all()
    elif not selected_category.exists() or not selected_ethnic.exists():
        return Food.objects.filter(Q(ethnic_food_name__in=selected_ethnic) | Q(category__in=selected_category)).distinct()
    return Food.objects.filter(ethnic_food_name__in=selected_ethnic).filter(category__in=selected_category).distinct()


def logging_user(request,selected_ethnic,selected_category):
    """
    Logging activities of users when they selected ethnic foods and categories.
    
    Args:
        selected_ethnic (EthinicFood): ethnic foods which have been chosen from user.
        selected_category (Category): categories which have been chosen from user.
    """
    user_ip = get_client_ip(request)
    category = str(selected_category)
    ethnic = str(selected_ethnic)

    if check_authenticated(request):
        user_id = request.user.id
        username = request.user.get_full_name()

        if not selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s id: %d user: %s didn\'t selected.' % (user_ip,user_id,username))
        elif selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s id: %d user: %s is selected %s.' % (user_ip,user_id,username,category))
        elif not selected_category.exists() and selected_ethnic.exists():
            logger.info('ip: %s id: %d user: %s is selected %s.' % (user_ip,user_id,username,ethnic))
        else:
            logger.info('ip: %s id: %d user: %s is selected %s and %s .' % (user_ip,user_id,username,ethnic,category))
    else:
        if not selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s Guest didn\'t selected.' % (user_ip))
        elif selected_category.exists() and not selected_ethnic.exists():
            logger.info('ip: %s Guest is selected %s.' % (user_ip,category))
        elif not selected_category.exists() and selected_ethnic.exists():
            logger.info('ip: %s Guest is selected %s.' % (user_ip,ethnic))
        else:
            logger.info('ip: %s Guest is selected %s and %s.' % (user_ip,ethnic,category))


def sort_food(unsorted_food):
    """
    Sort food by overall rate from users and rate in the database.
    
    Args:
        unsorted_food (list): a list of unsorted food.
    Returns:
        list: a list of sorted foods.
    """
    return sorted(unsorted_food, key = lambda food: food.set_total_rate(), reverse=True)[:25]


def check_vote(request,food_set):
    """
    Check that user is voted food or not.
    Set voteable's status for each food to be False if user is voted,
    True if otherwise. 

    Args:
        food_set (list): a list of foods.
    """
    for food in food_set:
        array = food.get_user_pk().split(',')
        if(str(request.user.pk) in array):
            food.set_check_false()
        else:
            food.set_check_true()
        food.save()


def vote_food(request,pk_food,vote):
    """
    Get vote score and primary key of food that user have been voted and update into the database.

    Args:
        pk_food (str): a primary key which use to specify food that has been voted.
        vote (str): text that use to specify rate value.
    """
    vote_scores = vote_value(vote)
    food = Food.objects.get(pk=pk_food)
    food.add_user_count()
    food.set_user_rate(vote_scores)
    food.add_user_pk(request.user.pk)
    food.save()


def check_authenticated(request):
    """
    Check that the account is authenticated or not.

    Returns:
        bool: True if the account is authenticated, False if otherwise.
    """
    return request.user.is_authenticated and not request.user.is_anonymous


class HomeView(TemplateView):
    """
    Homeview class render a template for a login page.
    """
    template_name = 'registration/login.html'


def IndexView(request):
    """
    IndexView class render an index page with the passed contexts.
    This class also represents all foods in the database.

    Returns:
        HttpResponse: an HttpResponse object with that rendered text.
    """
    user_ip = get_client_ip(request)
    template_name = 'khubkhaoapp/index.html'

    if check_authenticated(request):
        user_id = request.user.id
        username = request.user.get_full_name()
        logger.info('ip: %s id: %d user: %s have been using webpage.' % (user_ip,user_id,username))
        if request.method == "POST":
            my_vote = request.POST.get('rate_star')
            pk_and_vote = my_vote.split(',')
            vote_food(request,pk_and_vote[0],pk_and_vote[1])
            food = Food.objects.get(pk=pk_and_vote[0])
            rate = vote_value(pk_and_vote[1])
            logger.info('ip: %s id: %d user: %s have been vote %s for %s points.' % (user_ip,user_id,username,food,rate))
    else:
        logger.info('ip: %s Guest have been using webpage.' % user_ip)
    
    unsorted_results = Food.objects.all()
    check_vote(request,unsorted_results)
    if request.method == "POST":
        food_list = sort_food(unsorted_results)
    else :
        food_list = sorted(unsorted_results, key = lambda food: food.set_total_rate(), reverse=True)
    category_list = Category.objects.all()
    ethnic_list = EthnicFood.objects.all()
    context = {
        'food_list': food_list,
        'category_list': category_list,
        'ethnic_list': ethnic_list,
    }
    return render(request, template_name, context)
    

def IndexResultView(request):
    """
    IndexResultView class render an index page with the passed contexts and represents 25 foods
    in the database which filtered food's criteria specified by the user.

    Returns:
        HttpResponse: an HttpResponse object with that rendered text.
    """
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
