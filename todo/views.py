from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.


def get_todo_list(request):
    """
    Returns the basic to-do list page, passing to-do items.
    """
    results = Item.objects.all()
    return render(request, "todo_list.html", {"items": results})

def create_an_item(request):
    """
    Generates a form for the user to create a new item.
    """
    return render(request, "item_form.html")
