from django.urls import path
from . import views

# Routes
urlpatterns = [
	
	# /api
	path('', views.pingOverview, name="ping-overview"),

  ]