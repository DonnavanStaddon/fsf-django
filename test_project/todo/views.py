from django.shortcuts import render
from .models import Item

# Get to do list from db.
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

    # add item to db.
def add_item(request):
    return render(request, 'todo/add_item.html')