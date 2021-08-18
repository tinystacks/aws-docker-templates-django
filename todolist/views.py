from django.shortcuts import render,redirect
from .models import TodoList, Category, ItemList
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from todolist.serializers import UserSerializer, GroupSerializer, ItemSerializer

def index(request): #the index view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    items = ItemList.objects.all() #quering all items with the object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save() #saving the todo 
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
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
    if request.method == "DELETE":
        if "itemDelete" in request.DELETE: #checking if there is a request to delete a item
            checkedlist = request.DELETE["checkedbox"] #checked items to be deleted
            for item_id in checkedlist:
                item = ItemList.objects.get(id=int(item_id)) #getting item id
                item.delete() #deleting item
    return render(request, "index.html", {"todos": todos, "categories":categories, "items":items})

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
    queryset = ItemList.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
