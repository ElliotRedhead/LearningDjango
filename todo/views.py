from django.shortcuts import render, HttpResponse

# Create your views here.


def get_todo_list(request):
    """
    Returns the basic to-do list page.
    """
    return render(request, "todo_list.html")
