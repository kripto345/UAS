from django.urls import path
from .views import cipher_view

urlpatterns = [
    path('', cipher_view, name='cipher_view'),
]
