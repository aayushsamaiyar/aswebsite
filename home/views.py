from django import http
from django.shortcuts import render
from django.http.response import HttpResponse
from home.models import Contact, Projectpost
from django.contrib import messages

def home(request):
  return render(request,'portfolio/index.html')

def contact(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phoneno']
    mess = request.POST['message']
    if len(name)<2 or len(email)<3 or len(phone)<10 or len(mess)<4:
      messages.error(request,'please fill the details correctly.')
    else:
      contact = Contact(name = name, email = email, phone = phone, content= mess)
      contact.save()
      messages.success(request,'your message has been sent.')
  return render(request,'portfolio/contact.html')

def projects(request):
  myprojects = Projectpost.objects.all()
  return render(request,'portfolio/projects.html',{'myprojects':myprojects})

def resume(request):
  return render(request,'portfolio/resume.html')
