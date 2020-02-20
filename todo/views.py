from django.shortcuts import render, HttpResponse

# Create your views here.


def say_hello(request):
    """
    Creates a simple "Hello World" view to test if basic system is functioning.
    """
    return HttpResponse("Hello World")


def get_todo_list(request):
    """
    Returns the basic to-do list page.
    """
    return render(request, "todo_list.html")
