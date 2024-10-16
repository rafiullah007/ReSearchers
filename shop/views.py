from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,template_name='shop\home.html')


def profile(request):
    return render(request,template_name='shop\profile.html')

