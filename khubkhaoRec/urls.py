from django.contrib import admin
from django.urls import path, include
from khubkhaoapp.views import IndexResultView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('khubkhaoapp.urls')),
    path('result/', IndexResultView ),#Delete later because it must be called from index.html not by type in browser
]
