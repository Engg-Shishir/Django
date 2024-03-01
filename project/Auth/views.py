from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'Auth/register.html')
def login(request):
    return render(request,'Auth/login.html')
def logout(request):
    return 