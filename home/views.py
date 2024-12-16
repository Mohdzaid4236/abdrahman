from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def products(request):
    return render(request,'products.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def virtual(request):
    return render(request,'virtual.html')