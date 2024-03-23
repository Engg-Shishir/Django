from django.shortcuts import render

from .models import Author
# Create your views here.
def index(request):
    authors_with_social = Author.objects.prefetch_related('socials').all()
    return render(request,'index.html',{'data':authors_with_social})

def about(request):
    return render(request,'about.html')
def resume(request):
    return render(request,'resume.html')
def portfolio(request):
    return render(request,'portfolio.html')
def services(request):
    return render(request,'services.html')
def contact(request):
    return render(request,'contact.html')

def reverse(request):
    if request.method=="POST":
        input = request.POST.get('inp')
        output = input[::-1]

        dictionary={"input":input,"output":output}
    return render(request,'result.html',dictionary)
