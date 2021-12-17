from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse
from railapp import models
from accounts.models import Book
from .models import *
# Create your views here.
def home(request):
    if request.method=="POST":
        print("This is post")
        title = request.POST['title']
        content = request.POST['content']
        username = request.user.username
        print(username,title,content)
        ins = Announcement(username=username,title=title,content=content)
        ins.save()
        print("written successfully")
    post_list=Announcement.objects.order_by('created_on').reverse()
    post_list_2=Announcement.objects.latest('created_on')
    context = {'post_list':post_list, 'post_list_2':post_list_2}
    return render(request, 'railapp/home.html', context)

def contact(request):
    if request.method=="POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()


        send_mail(
             'message from' + name,
             subject,
             email,
             ['anjoomopshora@gmail.com'],

        )
        return render(request, 'railapp/contact.html', {'name' : name})
    else:
        return render(request, 'railapp/contact.html',{})
def checkout(request):
    return render(request, 'railapp/checkout.html')
def Confirmation(request):
    return render(request, 'railapp/confirmation.html')
def faq(request):
    content={}
    if request.user.is_authenticated:
        ques_obj = Questions.objects.all()
        ans_obj = Answers.objects.all()
        content={'ques_obj':ques_obj, 'ans_obj':ans_obj}
        return render(request, 'railapp/faq.html', content)
    
    
def userprofile(request,new={}):
    context = {}
    username_r = request.user.username
    book_list = Book.objects.filter(username=username_r)
    if book_list:
        return render(request, 'railapp/userprofile.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'railapp/userprofile.html', context)

def trainmasterprofile(request):
    return render(request, 'railapp/trainmasterprofile.html')
