from sys import prefix
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # Admin control
    path('my_app/', include('my_app.urls')), # 1 app
    path('first_app/', include('first_app.urls')), # 2 app
]




