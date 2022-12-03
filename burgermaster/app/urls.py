# 03.12.2022 Beginn: Initialisierung des Projektes #


from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
]