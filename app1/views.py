#coding=utf-8
from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect
from app1.models import User       #因为在app1下的操作，所以这里要写app1
from django import forms
#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',max_length=100)
    widget=forms.PasswordInput()
#登录
def login(request):
    if request.method =='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
#获取表单用户密码
            #获取的表单数据与数据库进行比较
            user=User.objects.filter(username__exact=username,password__exact=password)
            if user:
                return render_to_response('success.html',{'username':username})
            else:
                return render_to_response('fail.html',{'username':username})
    else:
        uf=UserForm()
    return  render_to_response('login.html',{'uf':uf})

