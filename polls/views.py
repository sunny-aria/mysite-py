from django.shortcuts import render

# Create your views here.

def hello(request):
    context = {}
    context['hello']='hello django!'
    return render(request,'hello.html',context)