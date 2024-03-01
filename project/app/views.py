from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def reverse(request):
    if request.method=="POST":
        input = request.POST.get('inp')
        output = input[::-1]

        dictionary={"input":input,"output":output}
    return render(request,'result.html',dictionary)
