# khubkhaoapp/urls.py

from django.urls import path
from khubkhaoapp.views import IndexView, IndexResultView, HomeView, IndexVoteView

app_name = 'khubkhaoapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('khubkhao/', IndexView.as_view(), name='index'),
    path('result/', IndexResultView, name='result'),
    path('vote/', IndexVoteView, name='vote'),

]