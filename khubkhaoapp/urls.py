from django.urls import path
from khubkhaoapp.views import IndexView, IndexResultView, HomeView


app_name = 'khubkhaoapp'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('khubkhao/', IndexView, name='index'),
    path('result/', IndexResultView, name='result'),
]
