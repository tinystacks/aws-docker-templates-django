from django.urls import path
from . import views

# Routes
urlpatterns = [
	
	# /api
	path('', views.apiOverview, name="api-overview"),
	
	# READ all the items
	# [GET] /api/item-list
	path('items/', views.itemList, name="item-list"),
	
	# READ a single item
	# [GET] /api/item-list/<id>
	path('items/<str:pk>/', views.itemDetail, name="item-list"),
	
	# CREATE a new item
	#[POST] /api/item-create
	path('item-create/', views.itemCreate, name="item-create"),
	
	# UPDATE an existing item
	#[PUT] /api/item-update/<id>
	path('item-update/<str:pk>/', views.itemUpdate, name="item-update"),
	
	#DELETE an existing item
	#[DELETE] /api/item-delete/<id>
	path('item-delete/<str:pk>/', views.itemDelete, name="item-delete"),
]