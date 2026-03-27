from django.http import HttpResponse
from django.shortcuts import render 

def home(request):
    return HttpResponse("Hello, World!")

def post_list(request):
    return render(request, 'blog/post_list.html', {})