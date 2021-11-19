from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('about',about,name='about'),
    path('portfolio',portfolio,name='portfolio'),
    path('contact',contact,name='contact'),
    path('<slug:portfolio_slug>',work),


]
