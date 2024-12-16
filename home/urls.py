from django.contrib import admin
from django.urls import path
from home import views 

urlpatterns = [
    path("",views.index,name='home'),
    path('products/',views.products,name='products'),
    path('blog/',views.blog,name='Blog'),
    path('about/',views.about,name='About Us'),
    path('gallery/',views.gallery,name='Gallery'),
    path('virtual/',views.virtual,name='Virtual Configurator'),
]
