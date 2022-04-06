from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item

@api_view(['GET'])
def apiOverview(request):
	return Response([
	 'READ all the items: /api/items',
	 'READ a single item: /api/items/<id>',
	 'CREATE a new item:  /api/item-create',
	 'UPDATE an item:     /api/item-update/<id>', 
	 'DELETE an item:     /api/item-delete/<id>'
	])

@api_view(['GET'])
def itemList(request):
	items = Item.objects.all().order_by('id')
	serializer = ItemSerializer(items, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def itemDetail(request, pk):
	items = Item.objects.get(id=pk)
	serializer = ItemSerializer(items, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
	serializer = ItemSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['PUT'])
def itemUpdate(request, pk):
	item = Item.objects.get(id=pk)
	serializer = ItemSerializer(instance=item, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def itemDelete(request, pk):
	item = Item.objects.get(id=pk)
	item.delete()
	return Response('Item deleted')