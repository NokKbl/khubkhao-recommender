# khubkhaoapp/urls.py

from django.urls import path
from khubkhaoapp.views import IndexView, IndexResultView, IndexVoteView

app_name = 'khubkhaoapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('result/', IndexResultView, name='result'),
    path('vote/', IndexVoteView, name='vote'),
]