from django.shortcuts import render

from .models import Author,Message
# Create your views here.
def index(request):
    authors_with_social = Author.objects.prefetch_related('socials', 'projects', 'testimonials').all()
    return render(request,'index.html',{'data':authors_with_social})

def about(request):
    authors_with_social = Author.objects.prefetch_related('socials','abouts').all()
    return render(request,'about.html',{'data':authors_with_social})

def resume(request):
    authors_with_resume = Author.objects.prefetch_related('education', 'experiance').all()
    return render(request,'resume.html',{'data':authors_with_resume})

def portfolio(request):
    return render(request,'portfolio.html')

def services(request):
    authors_with_services = Author.objects.prefetch_related('services').all()
    return render(request,'services.html',{'data':authors_with_services})

def contact(request):
    authors_with_resume = Author.objects.prefetch_related('contacts').all()
    return render(request,'contact.html',{'data':authors_with_resume})
    

def reverse(request):
    if request.method=="POST":
        input = request.POST.get('inp')
        output = input[::-1]

        dictionary={"input":input,"output":output}
    return render(request,'result.html',dictionary)


def save(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        tb = Message(name=name,email=email,subject=subject,msg=message)
        tb.save()


    authors_with_resume = Author.objects.prefetch_related('contacts').all()
    return render(request,'contact.html',{'data':authors_with_resume,'message':"Message send successfully !"})
