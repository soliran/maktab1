
from django.urls import path
from onepage.views import *

urlpatterns = [
    path('home', index),
    path('about', about),
    path('contact', contact),

]
