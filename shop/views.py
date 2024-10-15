from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='shop\home.html')

def products(request):
    return render(request,template_name='shop\products.html')

def products_details(request):
    return render(request,template_name='shop\products_details.html')