from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def IndexView(request):
    context = {

    }
    return render(request, 'khubkhaoapp/index.html', context)