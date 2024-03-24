# In profiles/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_list, name='user_list'),
    # Add this line for the search URL
]
