from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('api.urls')),
    path('api/', include('api.urls')),
    path('ping/', include('ping.urls')),
]