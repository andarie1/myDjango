from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_name, name='hello_name'), # Added view to the URL /my_app/hello
    ]
