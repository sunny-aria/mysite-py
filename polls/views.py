from django.shortcuts import render
from polls.models import Poll
# Create your views here.

def hello(request):
    context = {}
    context['hello']='hello django!'
    return render(request,'hello.html',context)

# 主页展示poll列表
def poll_index(request):
    poll_list = Poll.objects.all()
    return render(request,'poll/poll_list.html', {'pollList':poll_list})

def poll_edit(request,id):
    poll = Poll.objects.filter()
    return render(request,'poll/poll_edit.html',{'poll':poll})