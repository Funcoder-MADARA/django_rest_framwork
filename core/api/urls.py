from django.urls import path
from home.views import index  # Ensure this is correct

urlpatterns = [
    path('index/', index),
]