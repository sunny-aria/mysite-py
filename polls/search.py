# coding=utf-8
from django.http import HttpResponse

from django.shortcuts import render_to_response,render

from django.views.decorators.csrf import csrf_exempt
#表单
def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = "你搜索的内容为:" + request.GET['q']
    else:
        message = "你提交了空表单"
    return HttpResponse(message)
'''
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
对post请求要增加以上2行代码解决重复请求
html 页面要加入{% csrf_token %} 代码
'''

@csrf_exempt
def search_post(request):
    if request.POST:
        message = "你提交的内容为："+request.POST['q1']
    else:
        message ="你提交了空表单"
    context={}
    context['message']=message
    return render(request,'search_form.html',context)