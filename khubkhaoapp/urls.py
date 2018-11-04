# khubkhaoapp/urls.py

from django.urls import path
from khubkhaoapp.views import IndexView

app_name = 'khubkhaoapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]