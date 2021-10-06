from django.shortcuts import render,redirect
from .models import ItemList
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from itemslist.serializers import UserSerializer, GroupSerializer, ItemSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def index(request): #the index view
    items = ItemList.objects.all() #quering all items with the object manager
    if request.method == "POST": #checking if the request method is a POST
        if "itemAdd" in request.POST: #checking if there is a request to add a item
            title = request.POST["description"] #title
            content = title #content
            Item = ItemList(title=title, content=content)
            Item.save() #saving the item
            return redirect("/") #reloading the page
        if "itemDelete" in request.POST: #checking if there is a request to delete a item
            checkedlist = request.POST["checkedbox"] #checked items to be deleted
            for item_id in checkedlist:
                item = ItemList.objects.get(id=int(item_id)) #getting item id
                item.delete() #deleting item
    elif request.method == "DELETE": #checking if the request method is a DELETE
        if "itemDelete" in request.POST: #checking if there is a request to delete a item
            checkedlist = request.POST["checkedbox"] #checked items to be deleted
            for item_id in checkedlist:
                item = ItemList.objects.get(id=int(item_id)) #getting item id
                item.delete() #deleting item
    return render(request, "index.html", {"todos": todos, "categories":categories, "items":items})

@api_view(['GET', 'POST'])
def item_list(request): #the item_list view
    """
    List all items or create a new item
    """
    if request.method == 'GET': #checking if the request method is a GET
        items = ItemList.objects.all()
        serializer_context = {
            'request': request,
        }        
        serializer = ItemSerializer(items, many=True, context=serializer_context)
        return Response(serializer.data) #return all items
    elif request.method == 'POST': #checking if the request method is a POST
        serializer_context = {
            'request': request,
        }                
        serializer = ItemSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #return status if successful
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #return error if unsuccessful

@api_view(['GET', 'PUT', 'DELETE']) 
def item_detail(request, pk): #the item_detail view
    """
    Retrieve, update, or delete an item
    """
    try:
        item = ItemList.objects.get(pk=pk)
    except ItemList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': #checking if the request method is a GET
        serializer = ItemSerializer(item)
        return Response(item.data) #return all items
    elif request.method == 'PUT': #checking if the request method is a PUT
        serializer_context = {
            'request': request,
        }
        serializer = ItemSerializer(item, context=serializer_context)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) #return error if unsuccessful
    elif request.method == 'DELETE': #checking if the request is a DELETE
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) #return status 
        
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = ItemList.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
