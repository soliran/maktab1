
from django.urls import path
from onepage.views import *

urlpatterns = [
    path('', index),
    path('about', about),
    path('contact', contact),

]
