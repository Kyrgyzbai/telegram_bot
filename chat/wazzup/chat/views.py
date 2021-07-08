from django.shortcuts import render

# Create your views here.

def chat_view(request):
    return render(request, 'chat_page.html')

def login(request):
    return render(request, 'login.html')