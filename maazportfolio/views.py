from django.shortcuts import render

# Create your views here.
def maaz(request):
    return render(request,'index.html')