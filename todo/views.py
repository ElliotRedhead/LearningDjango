from django.shortcuts import render, HttpResponse

# Create your views here.
def ay_hello(request):
    return HttpResponse("Hello World")