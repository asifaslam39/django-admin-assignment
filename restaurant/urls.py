
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homePage, name='home'),
    path('upload/', views.upload_file, name='upload_file'),
    path('search/',views.searchPage,name='serach'),
]


# mainApp/urls.py
