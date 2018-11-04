from django.contrib import admin
from django.urls import path
from khubkhaoapp.views import IndexView, IndexResultView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('result/', IndexResultView ),#Delete later because it must be called from index.html not by type in browser
]
