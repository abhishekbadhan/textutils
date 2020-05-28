
from django.contrib import admin
from django.urls import path
from . import abhiitem1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', abhiitem1.front, name='front'),
    path('formresult', abhiitem1.result, name='formresult')
]
