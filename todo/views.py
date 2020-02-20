from django.shortcuts import render, HttpResponse

# Create your views here.
def day_hello(request):
    return HttpResponse("Hello World")