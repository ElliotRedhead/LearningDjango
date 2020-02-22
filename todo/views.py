from django.shortcuts import render, HttpResponse
from .models import Item

# Create your views here.


def get_todo_list(request):
    """
    Returns the basic to-do list page, passing to-do items.
    """
    results = Item.objects.all()
    return render(request, "todo_list.html", {"items": results})
